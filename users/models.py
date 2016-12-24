from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    note_to_santa = models.TextField(max_length=4200)
    steam = models.CharField(max_length=32, blank=True, null=True)
    # Whether or not the user has opted-in to Amazon Wishlist
    wishlist = models.CharField(max_length=120)
