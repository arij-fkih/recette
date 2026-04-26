# gestion_recette/gestion_recette/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recettes.urls')),          # ← inclure les URLs de l'app
]