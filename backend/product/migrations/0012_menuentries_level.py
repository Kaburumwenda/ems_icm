# Generated by Django 3.2.5 on 2021-07-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_submenu_menuentries'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuentries',
            name='level',
            field=models.CharField(default=0, max_length=255),
        ),
    ]
