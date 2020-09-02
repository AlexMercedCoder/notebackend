from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):

    message = models.CharField(max_length=140)

    class Meta:
        verbose_name_plural = 'notes'

    def __str__(self):
        return self.message


