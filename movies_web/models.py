from django.db import models


class AdditionalInfo(models.Model):
    GATUNEK = {
        (0, 'Inne'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-fi'),
        (4, 'Dramat'),
        (5, 'Przygodowy'),
        (6, 'Akcji'),
        (7, 'Kryminalny'),
        (8, 'Romans'),
        (9, 'Sensacyjny')
    }

    czas_trwania = models.PositiveSmallIntegerField(default=0)
    gatunek = models.PositiveSmallIntegerField(default=0, choices=GATUNEK)


class Movie(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    description = models.TextField(default='')
    premiere = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to='posters', null=True, blank=True)
    dodatkowe = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return '{} ({})'.format(self.title, self.year)


class Rating(models.Model):
    GWIAZDKI = {
        (1, '*'),
        (2, "**"),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    }
    recenzja = models.TextField(default='', blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=1, choices=GWIAZDKI)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.film




