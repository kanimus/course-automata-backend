from django.contrib import admin
from apps.user.models import Auth, School, User


admin.site.register(Auth)
admin.site.register(School)
admin.site.register(User)
