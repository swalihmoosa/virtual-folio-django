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
    permanent_state = models.CharField(max_length=125)
    permanent_district = models.CharField(max_length=125)
    current_state = models.CharField(max_length=125,default=permanent_state)
    current_disctrict = models.CharField(max_length=125,default=permanent_district)


    def __str__(self):
        return self.permanent_state

    class Meta:
        ordering = ["id"]



class Skill(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class SkillItems(models.Model):
    skill = models.ForeignKey("user.Skill",on_delete=models.CASCADE)
    rating = models.CharField(max_length=125)
    item = models.CharField(max_length=125)

    def __str__(self):
        return self.item

    class Meta:
        ordering = ["id"]


class Education(models.Model):
    year = models.CharField(max_length=125)
    course = models.CharField(max_length=125)
    university = models.CharField(max_length=125)
    description = models.TextField(max_length=125)

    def __str__(self):
        return self.course

    class Meta:
        ordering = ["id"]


class Experience(models.Model):
    year = models.CharField(max_length=125)
    work = models.CharField(max_length=125)
    company = models.CharField(max_length=125)
    description = models.TextField(max_length=125)

    def __str__(self):
        return self.work

    class Meta:
        ordering = ["id"]


class Client(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to="client/")
    company = models.CharField(max_length=125)
    description = models.TextField(max_length=125)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]