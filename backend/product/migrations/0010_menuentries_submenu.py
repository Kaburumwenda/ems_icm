# Generated by Django 3.2.5 on 2021-07-21 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='menuEntries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=255)),
                ('page', models.CharField(max_length=255)),
                ('isOpen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='submenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('page', models.CharField(max_length=255)),
            ],
        ),
    ]
