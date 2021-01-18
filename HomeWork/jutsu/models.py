from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Anime(models.Model):
    name = models.CharField(max_length=50)
    release_time = models.CharField(max_length=10)
    description = models.CharField(max_length=700)
    img = models.CharField(max_length=200)
    head_img = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, through='Anime_Genre')


    def __str__(self):
        return self.name


class Сharacter(models.Model):
    name = models.ForeignKey(Anime, on_delete=models.CASCADE)
    name_char = models.CharField(max_length=50)
    sag = models.CharField(max_length=100)
    side = models.CharField(max_length=100)
    img = models.CharField(max_length=200)


    def __str__(self):
        return self.name_char


class Anime_Genre(models.Model):
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)