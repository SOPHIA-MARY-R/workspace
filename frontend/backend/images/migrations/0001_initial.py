# Generated by Django 4.1.3 on 2023-02-08 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images')),
                ('rmbg_pic', models.ImageField(upload_to='images_rmbg')),
            ],
        ),
    ]