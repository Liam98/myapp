# Generated by Django 3.0.8 on 2020-07-30 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
