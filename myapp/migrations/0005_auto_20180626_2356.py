# Generated by Django 2.1a1 on 2018-06-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180626_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='max_range',
            field=models.IntegerField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_range',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
