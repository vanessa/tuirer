from django.db import models


class TuiteManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(content__icontains=query)
