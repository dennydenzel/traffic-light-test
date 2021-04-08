from django.db import models
from django.db.models.deletion import PROTECT


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
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'street', 'suite'],
                name='unique_address')
        ]


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    catchphrase = models.CharField(max_length=255)
    bs = models.CharField(max_length=255)


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    user = models.ForeignKey('User', on_delete=PROTECT, related_name='posts')
