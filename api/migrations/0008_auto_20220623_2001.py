# Generated by Django 3.2.5 on 2022-06-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rides_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='user',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='transaction_code',
            field=models.CharField(blank=True, default='G45DS8982GDF', max_length=255, null=True),
        ),
    ]
