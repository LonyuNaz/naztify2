# Generated by Django 5.0.2 on 2024-02-16 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naztify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
