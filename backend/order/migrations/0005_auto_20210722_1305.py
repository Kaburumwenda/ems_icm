# Generated by Django 3.2.5 on 2021-07-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210721_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
