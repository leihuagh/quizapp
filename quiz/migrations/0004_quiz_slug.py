# Generated by Django 2.1.5 on 2019-01-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190109_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
