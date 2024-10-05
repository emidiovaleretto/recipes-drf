from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-created_at')
    context = {
        'recipes': recipes
    }

    return render(request, 'recipes/index.html', context=context)


def category(request, slug):
    recipes = Recipe.objects.filter(category__category_slug=slug).filter(
        is_published=True).order_by('-created_at')
    context = {
        'recipes': recipes
    }

    return render(request, 'recipes/index.html', context=context)


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    ingredients = recipe.ingredients.split('\n')
    steps = recipe.preparation_steps.split('\n')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'steps': steps
    }

    return render(request, 'recipes/recipe-details.html', context=context)
