from django.db import models
from django.contrib.auth.models import User
from colorfield.fields import ColorField

# Create your models here.
class Categoria(models.Model):
    ID = models.CharField("ID", max_length=4, primary_key=True)
    nome = models.CharField("Nome", max_length=25, blank=False, null=False)
    colore = ColorField("Colore", default='#FF0000')
    descrizione = models.TextField("Descrizione", blank=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"

    def __str__(self):
        return self.nome


class Articolo (models.Model):
    ID = models.AutoField("ID", primary_key=True)
    titolo = models.CharField("Titolo", max_length=100, blank=False)
    autore = models.ForeignKey(User, verbose_name="Autore articolo", on_delete=models.CASCADE, blank=False, null=False, default="0")
    categoria = models.ForeignKey(Categoria, verbose_name="Categoria articolo", default="GLD", on_delete=models.CASCADE, blank=True)
    testo = models.TextField("Testo")

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"

    def __str__(self):
        return self.titolo

