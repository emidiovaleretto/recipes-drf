from django.shortcuts import render
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }

    return render(request, 'recipes/index.html', context=context)


def category(request, slug):
    recipes = Recipe.objects.filter(category__category_slug=slug)
    context = {
        'recipes': recipes
    }

    return render(request, 'recipes/index.html', context=context)


def recipe_detail(request, slug):
    recipe = Recipe.objects.filter(slug=slug)
    context = {
        'recipe': recipe
    }

    return render(request, 'recipes/recipe-details.html', context=context)
