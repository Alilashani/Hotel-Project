# Generated by Django 4.1.5 on 2023-01-30 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home_module', '0004_remove_startdate_user_delete_enddate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='USer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='نام')),
                ('family', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='تصویر آواتار')),
                ('email_active_code', models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')),
                ('about_user', models.TextField(blank=True, null=True, verbose_name='درباره شخص')),
                ('address', models.TextField(blank=True, null=True, verbose_name='آدرس')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن / نبودن')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
        migrations.CreateModel(
            name='StartDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('start_date', models.DateField(verbose_name='تاریخ ورود')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن / نبودن')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_module.user', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تاریخ ورود',
                'verbose_name_plural': 'تاریخ های ورود',
            },
        ),
        migrations.CreateModel(
            name='EndDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('end_date', models.DateField(verbose_name='تاریخ خروج')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن / نبودن')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_module.user', verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تاریخ خروج',
                'verbose_name_plural': 'تاریخ های خروج',
            },
        ),
    ]