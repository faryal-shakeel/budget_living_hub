from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clothing/', views.ClothingBrandListView.as_view(), name='clothing'),
    path('events/', views.LocalEventListView.as_view(), name='events'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('food/', views.FoodCentreListView.as_view(), name='food'),
    path('others/', views.OtherListView.as_view(), name='others'),
    path('sales/', views.UpcomingMegaSaleListView.as_view(), name='sales'),

    path('recipes/add/', views.RecipeCreate.as_view(), name='recipe-add'),
    path('clothing/add/', views.ClothingBrandCreate.as_view(), name='clothing-add'),
    path('events/add/', views.LocalEventCreate.as_view(), name='event-add'),
    path('food/add/', views.FoodCentreCreate.as_view(), name='food-add'),
    path('others/add/', views.OtherCreate.as_view(), name='other-add'),
    path('sales/add/', views.UpcomingMegaSaleCreate.as_view(), name='sale-add'),
]