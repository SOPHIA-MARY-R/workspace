# Generated by Django 4.1.3 on 2023-02-08 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='rmbg_pic',
            field=models.ImageField(blank=True, upload_to='images_rmbg'),
        ),
    ]