from django.contrib import admin
from .models import Categorie, Recette
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nombre_recettes')
    search_fields = ('nom',)

    def nombre_recettes(self, obj):
        return obj.recettes.count()
    nombre_recettes.short_description = "Nombre de recettes"


@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'duree_preparation', 'date_creation')
    list_filter = ('categorie',)
    search_fields = ('nom', 'ingredients')
    readonly_fields = ('date_creation',)
    fieldsets = (
        ('Informations générales', {
            'fields': ('nom', 'categorie', 'duree_preparation')
        }),
        ('Contenu', {
            'fields': ('ingredients', 'instructions')
        }),
        ('Métadonnées', {
            'fields': ('date_creation',)
        }),
    )