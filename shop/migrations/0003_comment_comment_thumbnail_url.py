# Generated by Django 2.1 on 2019-08-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190809_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_thumbnail_url',
            field=models.TextField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]