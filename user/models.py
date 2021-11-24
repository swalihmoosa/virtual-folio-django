from django.db import models
from django.db.models.base import Model

GENDER = (
    ("male","Male"),
    ("female","Female")
)


class Profile(models.Model):
    image = models.ImageField(upload_to="profile/images")
    name = models.CharField(max_length=125)
    profession = models.CharField(max_length=125)
    age = models.CharField(max_length=125)
    gender = models.CharField(max_length=125,choices=GENDER)
    resume = models.FileField(upload_to="profile/documents")
    description = models.TextField(max_length=255)
    address = models.ForeignKey("user.Address", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Address(models.Model):
    state = models.CharField(max_length=125)
    district = models.CharField(max_length=125)

    def __str__(self):
        return self.state

    class Meta:
        ordering = ["id"]



class Skill(models.Model):
    name = models.ForeignKey
