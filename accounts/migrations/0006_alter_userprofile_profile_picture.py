# Generated by Django 4.2.1 on 2023-06-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_address_line_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='userprofile/profile-picture.png', upload_to='userprofile'),
        ),
    ]