from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Recette, Categorie
from .forms import RecetteForm, CategorieForm


# ✅ Page d'accueil (+2pts)
def home(request):
    total_recettes = Recette.objects.count()
    total_categories = Categorie.objects.count()
    recettes_recentes = Recette.objects.order_by('-date_creation')[:3]
    return render(request, 'recettes/home.html', {
        'total_recettes': total_recettes,
        'total_categories': total_categories,
        'recettes_recentes': recettes_recentes,
    })


# ✅ Login (+2pts)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'recettes/login.html', {'erreur': 'Identifiants incorrects'})
    return render(request, 'recettes/login.html')


# ✅ Logout (+2pts)
def logout_view(request):
    logout(request)
    return redirect('login')


# ✅ Liste avec recherche (+1pt) et pagination (+1pt)
@login_required
def liste_recettes(request):
    recettes = Recette.objects.all().order_by('-date_creation')

    # Recherche
    query = request.GET.get('q', '')
    if query:
        recettes = recettes.filter(nom__icontains=query) | \
                   recettes.filter(ingredients__icontains=query) | \
                   recettes.filter(categorie__nom__icontains=query)

    # Pagination
    paginator = Paginator(recettes, 6)  # 6 recettes par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'recettes/liste_recettes.html', {
        'page_obj': page_obj,
        'query': query,
    })


@login_required
def ajouter_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES)  # ✅ request.FILES pour l'image
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm()
    return render(request, 'recettes/recette_form.html', {'form': form, 'titre': 'Ajouter une recette'})


@login_required
def modifier_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    if request.method == 'POST':
        form = RecetteForm(request.POST, request.FILES, instance=recette)  # ✅ request.FILES
        if form.is_valid():
            form.save()
            return redirect('liste_recettes')
    else:
        form = RecetteForm(instance=recette)
    return render(request, 'recettes/recette_form.html', {'form': form, 'titre': 'Modifier la recette'})


@login_required
def supprimer_recette(request, id):
    recette = get_object_or_404(Recette, id=id)
    if request.method == 'POST':
        recette.delete()
        return redirect('liste_recettes')
    return render(request, 'recettes/supprimer_recette.html', {'recette': recette})


@login_required
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'recettes/liste_categories.html', {'categories': categories})


@login_required
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'recettes/categorie_form.html', {'form': form, 'titre': 'Ajouter une catégorie'})


@login_required
def modifier_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'recettes/categorie_form.html', {'form': form, 'titre': 'Modifier la catégorie'})


@login_required
def supprimer_categorie(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'recettes/supprimer_categorie.html', {'categorie': categorie})