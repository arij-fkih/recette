# forms.py
from django import forms
from .models import Recette, Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']

class RecetteForm(forms.ModelForm):
    # Champ pour créer une nouvelle catégorie directement
    nouvelle_categorie = forms.CharField(
        max_length=100,
        required=False,
        label="Ou créer une nouvelle catégorie",
        help_text="Si vous tapez ici, elle sera créée et sélectionnée automatiquement"
    )

    class Meta:
        model = Recette
        fields = ['nom', 'categorie', 'ingredients', 'instructions', 'duree_preparation']

    def save(self, commit=True):
        nouvelle = self.cleaned_data.get('nouvelle_categorie')
        if nouvelle:
            cat, _ = Categorie.objects.get_or_create(nom=nouvelle.strip())
            self.instance.categorie = cat
        return super().save(commit)