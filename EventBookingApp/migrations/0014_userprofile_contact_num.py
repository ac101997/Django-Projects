# Generated by Django 5.1.1 on 2024-10-15 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventBookingApp', '0013_remove_userprofile_contact_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contact_num',
            field=models.PositiveBigIntegerField(default=None, null=True),
        ),
    ]
