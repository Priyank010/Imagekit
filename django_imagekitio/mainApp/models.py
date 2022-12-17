from django.db import models

class Photographers(models.Model):
    name = models.CharField(max_length=120)
    best_photo = models.CharField(max_length=120)
    photo_description = models.TextField(blank=True, null=True)
