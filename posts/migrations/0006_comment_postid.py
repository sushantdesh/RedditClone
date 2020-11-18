# Generated by Django 3.1.3 on 2020-11-09 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20201109_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='postid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='posts.posts'),
            preserve_default=False,
        ),
    ]