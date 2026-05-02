from django.urls import path
from . import views

urlpatterns = [
    # ✅ Page d'accueil (+2pts)
    path('', views.home, name='home'),

    # ✅ Authentification (+2pts)
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Recettes (existant)
    path('recettes/', views.liste_recettes, name='liste_recettes'),
    path('recettes/ajouter/', views.ajouter_recette, name='ajouter_recette'),
    path('recettes/modifier/<int:id>/', views.modifier_recette, name='modifier_recette'),
    path('recettes/supprimer/<int:id>/', views.supprimer_recette, name='supprimer_recette'),

    # Catégories (existant)
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/modifier/<int:id>/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/supprimer/<int:id>/', views.supprimer_categorie, name='supprimer_categorie'),
]