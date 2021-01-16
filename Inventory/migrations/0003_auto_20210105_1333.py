# Generated by Django 3.1 on 2021-01-05 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_auto_20210104_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(blank=True, choices=[('kg', 'kg'), ('dozen', 'dozen'), ('none', 'none')], default='none', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productbulkupload',
            name='csv_file',
            field=models.FileField(upload_to='inventory/bulkupload/'),
        ),
    ]
