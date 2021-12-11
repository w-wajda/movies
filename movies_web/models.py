from django.db import models


class AdditionalInfo(models.Model):
    INNY = 0
    HORROR = 1
    KOMEDIA = 2
    SCI_FI = 3
    DRAMAT = 4
    PRZYGODOWY = 5
    AKCJI = 6
    KRZYMINAL = 7
    ROMANS = 8
    SENSACYJNY = 9

    GATUNEK = {
        (INNY, 'Inne'),
        (HORROR, 'Horror'),
        (KOMEDIA, 'Komedia'),
        (SCI_FI, 'Sci-fi'),
        (DRAMAT, 'Dramat'),
        (PRZYGODOWY, 'Przygodowy'),
        (AKCJI, 'Akcji'),
        (KRZYMINAL, 'Kryminalny'),
        (ROMANS, 'Romans'),
        (SENSACYJNY, 'Sensacyjny')
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
    VERY_BAD = 0
    BAD = 1
    GOOD = 2
    VERY_GOOD = 3

    GWIAZDKI = [
        (VERY_BAD, 'Bardzo zły'),
        (BAD, "Zły"),
        (GOOD, 'Dobry'),
        (VERY_GOOD, 'Bardzo dobry'),
    ]

    recenzja = models.TextField(default='', blank=True)
    gwiazdki = models.PositiveSmallIntegerField(default=1, choices=GWIAZDKI)
    film = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Actor(models.Model):
    imie = models.CharField(max_length=20, blank=False)
    nazwisko = models.CharField(max_length=30, blank=False)
    filmy = models.ManyToManyField(Movie, related_name='actors')

    def __str__(self):
        return self.name_surname()

    def name_surname(self):
        return '{} {}'.format(self.imie, self.nazwisko)




