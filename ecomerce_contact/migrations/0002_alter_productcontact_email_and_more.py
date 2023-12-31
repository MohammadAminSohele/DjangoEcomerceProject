# Generated by Django 4.2.5 on 2023-09-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomerce_contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcontact',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='productcontact',
            name='full_name',
            field=models.CharField(max_length=150, verbose_name='نام و نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='productcontact',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='خوانده شده/ نشده'),
        ),
        migrations.AlterField(
            model_name='productcontact',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='productcontact',
            name='text',
            field=models.TextField(verbose_name='متن پیام'),
        ),
    ]
