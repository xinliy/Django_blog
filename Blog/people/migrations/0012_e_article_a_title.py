# Generated by Django 2.2 on 2019-04-24 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20190424_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='e_article',
            name='a_title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
