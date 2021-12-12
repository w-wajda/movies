# Generated by Django 3.2.9 on 2021-12-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_web', '0004_auto_20211202_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inne'), (1, 'Horror'), (5, 'Przygodowy'), (3, 'Sci-fi'), (9, 'Sensacyjny'), (4, 'Dramat'), (6, 'Akcji'), (8, 'Romans'), (7, 'Kryminalny'), (2, 'Komedia')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='gwiazdki',
            field=models.PositiveSmallIntegerField(choices=[(2, '**'), (4, '****'), (5, '*****'), (1, '*'), (3, '***')], default=1),
        ),
    ]