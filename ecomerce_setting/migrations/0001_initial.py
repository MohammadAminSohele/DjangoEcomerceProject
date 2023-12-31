# Generated by Django 4.2.5 on 2023-09-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان سایت')),
                ('address', models.CharField(max_length=100, verbose_name='ادرس')),
                ('phone', models.CharField(max_length=100, verbose_name='تلفن')),
                ('mobile', models.CharField(max_length=100, verbose_name='موبایل')),
                ('fax', models.CharField(max_length=100, verbose_name='فکس')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('about_us', models.TextField(verbose_name='درباره ما')),
                ('copy_right', models.CharField(blank=True, max_length=100, null=True, verbose_name='متن کپی رایت')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'مدیرت تنظیمات',
            },
        ),
    ]
