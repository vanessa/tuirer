from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.ManyToManyField('self', blank=True)
    following = models.ManyToManyField('self', blank=True)
    picture = models.ImageField('Foto de perfil', default='/img/blank-pic.png')
    created_at = models.DateTimeField(auto_now_add=True)

    liked_tuites = models.ManyToManyField('tuites.Tuite', related_name='liked_by')

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return self.following.count()
