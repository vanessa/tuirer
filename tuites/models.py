from django.db import models
from tuites.managers import TuiteManager


class Tuite(models.Model):
    content = models.CharField('Tweet', max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='tuites')

    objects = TuiteManager()

    class Meta:
        ordering = ('-date_created', )

    @property
    def likes_count(self):
        return self.liked_by.count()

    def __str__(self):
        return '@{author}: {content}'.format(
            author=self.creator.username,
            content=self.content
        )
