# Generated by Django 3.2.9 on 2021-12-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_web', '0008_auto_20211211_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Przygodowy'), (2, 'Komedia'), (3, 'Sci-fi'), (9, 'Sensacyjny'), (1, 'Horror'), (0, 'Inne'), (7, 'Kryminalny'), (6, 'Akcji'), (8, 'Romans'), (4, 'Dramat')], default=0),
        ),
    ]
