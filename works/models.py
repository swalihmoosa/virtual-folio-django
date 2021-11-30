from django.db import models
from django.db.models.fields.files import ImageField


class Service(models.Model):
    image = models.FileField(upload_to="service/")
    title = models.CharField(max_length=125)
    description = models.TextField(max_length=355)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


class Category(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]


class Project(models.Model):
    thumbnail = models.FileField(upload_to="project/thumb")
    feature_image = models.ImageField(upload_to="project/feature_image")
    title = models.CharField(max_length=125)
    is_completed = models.BooleanField(default=False)
    is_satisfied = models.BooleanField(default=False)
    category = models.ForeignKey("works.category", on_delete=models.CASCADE)
    clients = models.ForeignKey("user.client",on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
