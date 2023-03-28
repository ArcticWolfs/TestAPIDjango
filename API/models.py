from django.db import models

# Create your models here.


class Author(models.Model):
    firstname = models.CharField(max_length=100, verbose_name="Prénom")
    lastname = models.CharField(max_length=100, verbose_name="Nom")
    nationality = models.CharField(max_length=200, verbose_name="Nationalité")

    class Meta:
        verbose_name = "Auteur"


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name="Titre")
    price = models.DecimalField(verbose_name="Prix", max_digits=6, decimal_places=2)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
