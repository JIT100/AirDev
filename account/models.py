from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
# Create your models here.

User = get_user_model()

class BlackListedToken(models.Model):
    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name="token_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("token", "user")
