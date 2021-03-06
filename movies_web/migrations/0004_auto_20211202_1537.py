# Generated by Django 3.2.9 on 2021-12-02 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies_web', '0003_auto_20211202_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='gatunek',
            field=models.PositiveSmallIntegerField(choices=[(8, 'Romans'), (7, 'Kryminalny'), (0, 'Inne'), (3, 'Sci-fi'), (2, 'Komedia'), (6, 'Akcji'), (1, 'Horror'), (9, 'Sensacyjny'), (4, 'Dramat'), (5, 'Przygodowy')], default=0),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recenzja', models.TextField(blank=True, default='')),
                ('gwiazdki', models.PositiveSmallIntegerField(choices=[(4, '****'), (5, '*****'), (1, '*'), (2, '**'), (3, '***')], default=1)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies_web.movie')),
            ],
        ),
    ]
