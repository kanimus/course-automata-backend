from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import CustomUserManager


class School(models.Model):
    name = models.CharField(max_length=50, verbose_name='School name')
    short_name = models.CharField(max_length=10, verbose_name="Short name")
    name_nationalized = models.CharField(max_length=50, verbose_name='Nationalized name')
    short_name_nationalized = models.CharField(max_length=10, verbose_name="Short Nationalized name")

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'


class User(AbstractBaseUser, PermissionsMixin):

    google_id = models.IntegerField(null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'id'

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Auth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user_school_id = models.CharField(max_length=40, verbose_name="User's school id")
    login = models.CharField(max_length=120, verbose_name="User school login")
    password = models.CharField(max_length=120, verbose_name="User school password")
    isAuthenticated = models.BooleanField(default=True)  # To default token already created for user

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Auth'
        verbose_name_plural = 'Auths'


