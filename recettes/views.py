# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recette, Categorie
from .forms import RecetteForm, CategorieForm


def liste_recettes(request):
    recettes = Recette.objects.all()
    return render(request, 'recettes/liste.html', {'recettes': recettes})


def ajouter_recette(request):
    if request.method == "POST":
        form = RecetteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm()
    return render(request, 'recettes/form.html', {'form': form, 'titre': 'Ajouter une recette'})


def modifier_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    if request.method == "POST":
        form = RecetteForm(request.POST, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm(instance=recette)
    return render(request, 'recettes/form.html', {'form': form, 'titre': 'Modifier la recette'})


def supprimer_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    if request.method == "POST":
        recette.delete()
        return redirect('liste_recettes')
    return render(request, 'recettes/confirmer_suppression.html', {'recette': recette})


def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'recettes/categories.html', {'categories': categories})


def ajouter_categorie(request):
    if request.method == "POST":
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'recettes/categorie_form.html', {'form': form, 'titre': 'Ajouter une catégorie'})


def modifier_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == "POST":
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'recettes/categorie_form.html', {'form': form, 'titre': 'Modifier la catégorie'})


def supprimer_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == "POST":
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'recettes/confirmer_suppression_categorie.html', {'categorie': categorie})