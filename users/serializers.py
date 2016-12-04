from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import User

alpha_only = RegexValidator('^[A-Za-z0-9_]+$', message='Illegal Characters!')


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[alpha_only])
    password = serializers.CharField(style={'input_type': 'password'})
    note_to_santa = serializers.CharField()

    def create(self, validated_data):
        user = validated_data.pop('username', None)
        passwd = validated_data.pop('password', None)
        to_santa = validated_data.pop('note_to_santa', None)

        does_exist = User.objects.filter(username__iexact=user)
        if len(does_exist) > 0:
            return

        instance = User(username = user, note_to_santa = to_santa)
        if passwd:
            instance.set_password(passwd)
            instance.save()
            return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
