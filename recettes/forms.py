from django import forms
from .models import Recette, Categorie


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RecetteForm(forms.ModelForm):
    nouvelle_categorie = forms.CharField(
        max_length=100,
        required=False,
        label="Ou créer une nouvelle catégorie",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Recette
        fields = ['nom', 'categorie', 'ingredients', 'instructions', 'duree_preparation', 'image']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'ingredients': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'instructions': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'duree_preparation': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        nouvelle = self.cleaned_data.get('nouvelle_categorie')
        if nouvelle:
            cat, _ = Categorie.objects.get_or_create(nom=nouvelle.strip())
            self.instance.categorie = cat
        return super().save(commit)