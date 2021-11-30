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