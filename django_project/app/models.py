from django.db import models
from django.core.validators import MinLengthValidator

class Country(models.Model):
    name = models.CharField(max_length=100)
    iso_code = models.CharField(unique=True, max_length=3, validators=[MinLengthValidator(3)])
    population = models.IntegerField()

    def __str__(self):
        return self.name
