from django.db import models
from django.db.models.deletion import PROTECT
from django.core.validators import MaxValueValidator, MinValueValidator 


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=32)
    website = models.URLField()

    address = models.ForeignKey('Address', on_delete=PROTECT, related_name='users')
    company = models.ForeignKey('Company', on_delete=PROTECT, related_name='users')


class Address(models.Model):
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)
    lat = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    lng = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])


class Company(models.Model):
    name = models.CharField(max_length=255)
    catchphrase = models.CharField(max_length=255)
    bs = models.CharField(max_length=255)


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    body = models.TextField(blank=True)

    user = models.ForeignKey('Users', on_delete=PROTECT, related_name='posts')
