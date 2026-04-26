# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Recettes
    path('', views.liste_recettes, name='liste_recettes'),
    path('ajouter/', views.ajouter_recette, name='ajouter_recette'),
    path('modifier/<int:id>/', views.modifier_recette, name='modifier_recette'),
    path('supprimer/<int:id>/', views.supprimer_recette, name='supprimer_recette'),

    # Catégories
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
]