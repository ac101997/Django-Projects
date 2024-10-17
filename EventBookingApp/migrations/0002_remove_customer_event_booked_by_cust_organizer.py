# Generated by Django 5.1.1 on 2024-10-14 06:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventBookingApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='event_booked_by_cust',
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('organizer_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='organizer_profile', to='EventBookingApp.userprofile')),
            ],
        ),
    ]
