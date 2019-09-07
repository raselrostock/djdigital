from django.db import models


class SubscribeModel(models.Model):
    email = models.EmailField(null=False, blank=True,
                              max_length=200, unique=True)
    status = models.CharField(max_length=64, null=False, blank=True)
    created_date = models.DateTimeField(null=False, blank=True)
    updated_date = models.DateTimeField(null=False, blank=True)

    def __str__(self):
        return self.email
