# Generated by Django 4.2.5 on 2023-09-20 17:38

from django.db import migrations, models
import django.db.models.deletion
import ecomerce_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce_products', '0004_product_catagories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to=ecomerce_products.models.upload_gallary_image_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomerce_products.product')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]
