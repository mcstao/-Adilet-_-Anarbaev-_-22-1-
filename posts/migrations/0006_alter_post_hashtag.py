# Generated by Django 4.1.3 on 2022-11-22 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_rename_disciption_post_desciption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hashtag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.hashtag'),
        ),
    ]
