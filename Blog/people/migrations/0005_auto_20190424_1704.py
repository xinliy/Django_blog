# Generated by Django 2.2 on 2019-04-24 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20190424_1552'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Article',
        ),
    ]