# Generated by Django 3.1.2 on 2020-10-28 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('user', '0001_initial'), ('user', '0002_authtoken'), ('user', '0003_auto_20201024_1152'), ('user', '0004_auth_isauthenticated'), ('user', '0005_remove_auth_isauthenticated'), ('user', '0006_auto_20201028_0758')]

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('google_id', models.IntegerField(null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='School name')),
                ('short_name', models.CharField(max_length=10, verbose_name='Short name')),
                ('name_nationalized', models.CharField(max_length=50, verbose_name='Nationalized name')),
                ('short_name_nationalized', models.CharField(max_length=10, verbose_name='Short Nationalized name')),
            ],
            options={
                'verbose_name': 'School',
                'verbose_name_plural': 'Schools',
            },
        ),
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_school_id', models.CharField(max_length=40, verbose_name="User's school id")),
                ('login', models.CharField(max_length=120, verbose_name='User school login')),
                ('password', models.CharField(max_length=120, verbose_name='User school password')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.school')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Auth',
                'verbose_name_plural': 'Auths',
            },
        ),
    ]
