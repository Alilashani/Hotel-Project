# Generated by Django 4.1.5 on 2023-03-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0025_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100, verbose_name='نام وبسایت')),
                ('site_url', models.CharField(max_length=100, verbose_name='دامنه وبسایت')),
                ('address', models.CharField(max_length=100, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='تلفن ')),
                ('fax', models.CharField(blank=True, max_length=100, null=True, verbose_name='فکس ')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='ایمیل ')),
                ('copy_right', models.TextField(verbose_name='متن کپی رایت وبسایت')),
                ('about_us_text', models.TextField(verbose_name='متن درباره ما سایت')),
                ('site_logo', models.ImageField(upload_to='images/site_setting', verbose_name='لوگو سایت')),
                ('is_main_setting', models.BooleanField(verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]