# Generated by Django 5.0.2 on 2024-03-06 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naztify', '0004_weeklyupdatesubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='weekly_update',
            field=models.BooleanField(default=False),
        ),
    ]
