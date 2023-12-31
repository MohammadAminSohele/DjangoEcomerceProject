# Generated by Django 4.2.5 on 2023-09-10 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecomerce_products', '0003_alter_product_options_alter_product_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('slug', models.SlugField(verbose_name='عنوان در url')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('activate', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('product', models.ManyToManyField(blank=True, to='ecomerce_products.product', verbose_name='محصولات')),
            ],
        ),
    ]
