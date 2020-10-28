from django.contrib import admin

from apps.user.models import User, School, Auth

admin.site.register(User)
admin.site.register(School)
admin.site.register(Auth)
