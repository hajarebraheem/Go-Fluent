# Generated by Django 3.2.2 on 2021-05-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='goal',
            field=models.TextField(max_length=140, null=True),
        ),
    ]
