from django.db import models
from django.db.models.base import Model

from user.models import Client


class Testimonial(models.Model):
    client = models.ForeignKey("user.client", on_delete=models.CASCADE)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.client

    class Meta:
        ordering = ["id"]


class Contact(models.Model):
    name = models.CharField(max_length=125)
    email = models.EmailField()
    subject = models.CharField(max_length=125)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ["id"]


class Login(models.Model):
    username = models.CharField(max_length=125)
    password = models.CharField(max_length=125)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["id"]


class Signup(models.Model):
    name = models.CharField(max_length=125)
    username = models.CharField(max_length=125)
    password = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]