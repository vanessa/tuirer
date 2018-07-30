from django.db import models
from users.models import User


class TuiteManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(content__icontains=query)
