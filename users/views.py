from django.shortcuts import render
from rest_framework import viewsets, permissions

from .models import User
from .serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        params = self.request.query_params
        query = User.objects.all()

        if 'memes' in params:
            query = User.objects.filter(note_to_santa__icontains='memes')
        return query
