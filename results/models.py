from django.db import models
from users.models import User


class Result(models.Model):
    poster = models.ForeignKey(User)
    image = models.ImageField(upload_to='/cdn/presents')
    santa = models.ForeignKey(User, related_name='santa_nigga')
