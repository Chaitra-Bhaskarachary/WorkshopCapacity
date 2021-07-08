# Create your models here.
import datetime
from django.db import models
from django.core.validators import (MinValueValidator, MaxValueValidator, FileExtensionValidator)

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)    

class WorkshopCapacity(models.Model):

    admin_id = models.CharField(
        max_length=100,
        blank=False,
        null=False
    )
    admin_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    calender_week = models.IntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(1), MaxValueValidator(53)]
    )
    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[MinValueValidator(2000), max_value_current_year]
    )
    entry_check = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]    
    )
    exit_check = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )
    retail_ready = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0)]
    )




