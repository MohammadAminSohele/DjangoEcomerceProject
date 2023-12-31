# Generated by Django 4.2.5 on 2023-09-27 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecomerce_products', '0006_alter_productgallary_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_payid', models.BooleanField(default=False, verbose_name='خریداری شده / نشده')),
                ('date_payid', models.DateTimeField(verbose_name='تاریخ پرداخت')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبد های  خرید کاربران',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('count', models.IntegerField(verbose_name='تعداد')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomerce_order.order', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomerce_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'اطلاعات جزییات سبد خرید کاربر',
                'verbose_name_plural': 'اطلاعات جزییات سبد های خرید کاربران',
            },
        ),
    ]
