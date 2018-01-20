from django.db import models
from django.contrib.auth import models as m
# Create your models here.
class myUser(m.User,m.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
