# Generated by Django 3.1 on 2021-01-15 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_salesitem_sale_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesitem',
            name='sale_code',
        ),
    ]
