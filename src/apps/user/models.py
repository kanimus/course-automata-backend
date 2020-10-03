from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager


class School(models.Model):
    name = models.CharField(max_length=50, verbose_name='School name')
    short_name = models.CharField(max_length=10, verbose_name="Short name")

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'


class User(AbstractBaseUser, PermissionsMixin):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    user_school_id = models.IntegerField(default=0)
    login = models.CharField(max_length=120, verbose_name="User school login")
    password = models.CharField(max_length=120, verbose_name="User school password")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'id'

    # @property
    # def isAuthenticated(self):
    #     return True if self.auth_id else False

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Auth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    google_id = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Auth'
        verbose_name_plural = 'Auths'