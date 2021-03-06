# Generated by Django 3.2.5 on 2022-06-12 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='comments',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='rides',
            name='destination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rides',
            name='sorce',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='rides',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rides', to=settings.AUTH_USER_MODEL),
        ),
    ]
