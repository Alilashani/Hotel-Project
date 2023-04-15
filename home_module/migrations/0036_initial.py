# Generated by Django 4.1.5 on 2023-03-11 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_module', '0008_initial'),
        ('home_module', '0035_delete_aboutsite_remove_booking_room_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام')),
                ('description', models.CharField(max_length=1000, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='نام')),
                ('email', models.EmailField(max_length=500, verbose_name='ایمیل')),
                ('massage', models.CharField(max_length=1000, verbose_name='متن')),
                ('massage_admin', models.CharField(max_length=1000, verbose_name='متن ادمین')),
                ('see_text', models.BooleanField(default=False, verbose_name='دیده شده / نشده')),
            ],
            options={
                'verbose_name': 'ارتباط با ما',
                'verbose_name_plural': 'ارتباتاط با ما',
            },
        ),
        migrations.CreateModel(
            name='FoodsHotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='نام')),
                ('description', models.CharField(max_length=1000, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'تنظیمات غذا',
                'verbose_name_plural': 'تنظیمات غذا ها',
            },
        ),
        migrations.CreateModel(
            name='Moshtari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='نام')),
                ('description', models.CharField(max_length=1000, verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتری ها',
            },
        ),
        migrations.CreateModel(
            name='SettingSite_header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=3000, verbose_name='نام')),
                ('description', models.CharField(max_length=1000, verbose_name='توضیحات')),
                ('address', models.CharField(max_length=10000, verbose_name='آدرس')),
                ('title_room', models.CharField(max_length=500, verbose_name='نام اتاق')),
                ('description_room', models.CharField(max_length=1000, verbose_name='توضیحات اتاق')),
                ('is_main_setting', models.BooleanField(default=True, verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیم بالای سایت',
                'verbose_name_plural': 'تنظیمات بالای سایت',
            },
        ),
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
                ('site_logo', models.ImageField(upload_to='uploads/site_setting', verbose_name='لوگو سایت')),
                ('is_main_setting', models.BooleanField(verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rooms', models.CharField(max_length=60, verbose_name='تعداد اتاق')),
                ('room_type', models.CharField(max_length=60, verbose_name='نوع اتاق')),
                ('price', models.CharField(max_length=5000, verbose_name='قیمت')),
                ('score', models.IntegerField(verbose_name='شناسه')),
                ('start_date', models.DateField(verbose_name='تاریخ ورود')),
                ('room_image', models.ImageField(upload_to='uploads', verbose_name='عکس اتاق ها')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('manager', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_module.user', verbose_name='کاربران')),
            ],
            options={
                'verbose_name': 'اتاق',
                'verbose_name_plural': 'اتاق ها',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='نام')),
                ('email', models.EmailField(max_length=500, verbose_name='ایمیل')),
                ('massage', models.CharField(max_length=1000, verbose_name='متن')),
                ('massage_admin', models.CharField(max_length=1000, verbose_name='متن ادمین')),
                ('see_text', models.BooleanField(default=False, verbose_name='دیده شده / نشده')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_module.admin', verbose_name='توسط ادمین')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'لیست تماس با ما',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='تاریخ ورود')),
                ('end_date', models.DateField(verbose_name='تاریخ خروج')),
                ('booked_on', models.DateField(verbose_name='رزرو')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_module.rooms', verbose_name='تعداد اتاق ها')),
            ],
            options={
                'verbose_name': 'رزرو',
                'verbose_name_plural': 'لیست رزرو ها',
            },
        ),
    ]
