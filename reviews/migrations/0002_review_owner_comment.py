# Generated by Django 3.2.6 on 2021-08-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='owner_comment',
            field=models.TextField(null=True),
        ),
    ]