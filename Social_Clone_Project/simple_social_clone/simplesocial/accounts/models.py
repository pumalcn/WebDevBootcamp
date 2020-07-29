from django.contrib.auth.models import User, PermissionsMixin

from django.db import models
from django.utils import timezone


class BaseUser(User, PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
