from django.db import models

# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=7, default='#FFFFFF')  # Белый цвет по умолчанию

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    colors = models.ManyToManyField(Color, related_name='items')  

    def __str__(self):
        return self.name