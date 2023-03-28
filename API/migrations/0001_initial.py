# Generated by Django 4.1.7 on 2023-03-27 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, verbose_name='Prénom')),
                ('lastname', models.CharField(max_length=100, verbose_name='Nom')),
                ('nationality', models.CharField(max_length=200, verbose_name='Nationalité')),
            ],
            options={
                'verbose_name': 'Auteur',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Titre')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Prix')),
                ('description', models.TextField()),
            ],
        ),
    ]