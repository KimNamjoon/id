# Generated by Django 2.2.11 on 2020-04-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0015_merge_20200416_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date',
            field=models.CharField(default='2020-04-16-19.03.39', max_length=100),
        ),
    ]
