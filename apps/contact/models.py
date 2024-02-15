from django.db import models


class Branch(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    location = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class GetInTouch(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name
