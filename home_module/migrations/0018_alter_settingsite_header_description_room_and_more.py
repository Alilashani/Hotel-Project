# Generated by Django 4.1.5 on 2023-03-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0017_settingsite_header_description_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsite_header',
            name='description_room',
            field=models.CharField(max_length=1000, verbose_name='توضیحات اتاق'),
        ),
        migrations.AlterField(
            model_name='settingsite_header',
            name='title_room',
            field=models.CharField(max_length=500, verbose_name='نام اتاق'),
        ),
    ]