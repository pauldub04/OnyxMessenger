# Generated by Django 3.1.7 on 2021-05-28 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsession',
            name='title',
            field=models.TextField(default='Chat'),
            preserve_default=False,
        ),
    ]
