# Generated by Django 4.1.3 on 2022-11-21 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='disciption',
            new_name='desciption',
        ),
    ]
