# Generated by Django 3.2.3 on 2021-05-24 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='stockid',
            new_name='stock',
        ),
    ]
