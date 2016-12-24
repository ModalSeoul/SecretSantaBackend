from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import User

alpha_only = RegexValidator('^[A-Za-z0-9_]+$', message='Illegal Characters!')


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[alpha_only])
    password = serializers.CharField(style={'input_type': 'password'})
    steam = serializers.CharField()
    wishlist = serializers.CharField()
    note_to_santa = serializers.CharField()

    def create(self, validated_data):
        user = validated_data.pop('username', None)
        passwd = validated_data.pop('password', None)
        note_to_santa = validated_data.pop('note_to_santa', None)
        wishlist = validated_data.pop('wishlist', None)
        steam = validated_data.pop('steam', None)


        does_exist = User.objects.filter(username__iexact=user)

        if len(does_exist) > 0:
            return

        instance = User(
            username=user,
            note_to_santa=note_to_santa,
            steam=steam,
            wishlist=wishlist)

        if passwd:
            print('HIT')
            instance.set_password(passwd)
        else:
            print('No password')
        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
