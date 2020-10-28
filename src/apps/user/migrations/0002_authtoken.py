# Generated by Django 3.1.2 on 2020-10-19 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.auth')),
            ],
            options={
                'verbose_name': 'AuthToken',
                'verbose_name_plural': 'AuthTokens',
            },
        ),
    ]