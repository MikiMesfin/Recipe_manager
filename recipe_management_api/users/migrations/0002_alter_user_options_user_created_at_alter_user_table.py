# Generated by Django 5.1 on 2024-12-26 15:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 12, 26, 15, 29, 33, 953288, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='user',
            table=None,
        ),
    ]
