from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TodoList(models.Model):
    task = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True , blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task

@receiver(post_save , sender=User)
def creste_auth_token(sender , instance=None,created=False , **kwargs):
    if created:
        Token.objects.create(user=instance)

