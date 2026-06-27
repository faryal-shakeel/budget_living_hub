from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .models import ClothingBrand, LocalEvent, Recipe, FoodCentre, Other, UpcomingMegaSale


def index(request):
    """Home page showing counts of each model."""
    num_clothing = ClothingBrand.objects.count()
    num_events = LocalEvent.objects.count()
    num_recipes = Recipe.objects.count()
    num_food = FoodCentre.objects.count()
    num_other = Other.objects.count()
    num_sales = UpcomingMegaSale.objects.count()

    context = {
        'num_clothing': num_clothing,
        'num_events': num_events,
        'num_recipes': num_recipes,
        'num_food': num_food,
        'num_other': num_other,
        'num_sales': num_sales,
    }

    return render(request, 'index.html', context=context)

class ClothingBrandListView(generic.ListView):
    model = ClothingBrand
    template_name = 'clothingbrand_list.html'


class LocalEventListView(generic.ListView):
    model = LocalEvent
    template_name = 'localevent_list.html'


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = 'recipe_list.html'


class FoodCentreListView(generic.ListView):
    model = FoodCentre
    template_name = 'foodcentre_list.html'


class OtherListView(generic.ListView):
    model = Other
    template_name = 'other_list.html'

# Recipe add — open to EVERYONE (no login needed)
class RecipeCreate(generic.CreateView):
    model = Recipe
    fields = ['recipe_name', 'description', 'cost']
    template_name = 'recipe_form.html'
    success_url = '/recipes/'


# The other four — only logged-in users can add
class ClothingBrandCreate(LoginRequiredMixin, generic.CreateView):
    model = ClothingBrand
    fields = ['brand_name', 'description', 'location']
    template_name = 'clothingbrand_form.html'
    success_url = '/clothing/'


class LocalEventCreate(LoginRequiredMixin, generic.CreateView):
    model = LocalEvent
    fields = ['event_name', 'date', 'specification', 'location']
    template_name = 'localevent_form.html'
    success_url = '/events/'


class FoodCentreCreate(LoginRequiredMixin, generic.CreateView):
    model = FoodCentre
    fields = ['cafe_name', 'description', 'location']
    template_name = 'foodcentre_form.html'
    success_url = '/food/'


class OtherCreate(LoginRequiredMixin, generic.CreateView):
    model = Other
    fields = ['product_name', 'shop_location', 'description']
    template_name = 'other_form.html'
    success_url = '/others/'

class UpcomingMegaSaleListView(generic.ListView):
    model = UpcomingMegaSale
    template_name = 'upcomingmegasale_list.html'


class UpcomingMegaSaleCreate(LoginRequiredMixin, generic.CreateView):
    model = UpcomingMegaSale
    fields = ['brand', 'start_date', 'end_date', 'discount']
    template_name = 'upcomingmegasale_form.html'
    success_url = '/sales/'