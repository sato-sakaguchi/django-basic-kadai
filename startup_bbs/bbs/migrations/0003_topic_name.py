# Generated by Django 4.1.5 on 2023-11-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_topic_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default='noname', max_length=100, verbose_name='投稿者の名前'),
            preserve_default=False,
        ),
    ]
