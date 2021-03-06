# Generated by Django 2.0.3 on 2021-07-07 08:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkshopCapacity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=100)),
                ('admin_name', models.CharField(blank=True, max_length=150, null=True)),
                ('calender_week', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(53)])),
                ('entry_check', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('exit_check', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('retail_ready', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
