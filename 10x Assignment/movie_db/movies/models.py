from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Technician(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    rating = models.FloatField()
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)
    technicians = models.ManyToManyField(Technician)

    def __str__(self):
        return self.name
