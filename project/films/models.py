from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length = 150)
    

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=250)
    length = models.PositiveIntegerField(blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0),MaxValueValidator(10)])
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self))
            if field.verbose_name != 'genre'

            else 
                (field.verbose_name, Genre.objects.get(pk=field.value_from_object(self)).name)

            for field in self.__class__._meta.fields[1:]
        ]