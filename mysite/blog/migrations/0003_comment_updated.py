# Generated by Django 4.0.4 on 2022-05-03 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
