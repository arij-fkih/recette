from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.nom


class Recette(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    duree_preparation = models.IntegerField(help_text="Durée en minutes")
    date_creation = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="recettes"
    )
    # ✅ NOUVEAU : champ image (+1pt)
    image = models.ImageField(upload_to='recettes/', blank=True, null=True)

    def __str__(self):
        return self.nom