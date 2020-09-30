from django.db import models
from django.contrib.auth.models import AbstractUser


class School(models.Model):
    name = models.CharField(max_length=50, verbose_name='School name')
    short_name = models.CharField(max_length=10, verbose_name="Short name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'Schools'


class User(AbstractUser):
    google_id = models.IntegerField()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Auth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    user_school_id = models.IntegerField()
    login = models.CharField(max_length=120, verbose_name="User school login")
    password = models.CharField(max_length=120, verbose_name="User school password")
    isAuthenticated = models.BooleanField(default=False)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Auth'
        verbose_name_plural = 'Auths'
