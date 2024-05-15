from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('fuels/', views.FuelListView.as_view(), name='fuel-list'),
    path('fuels/create/', views.FuelCreateView.as_view(), name='fuel-create'),
    path('fuelstations/', views.FuelStationListView.as_view(), name='fuelstation-list'),
    path('fuelstations/create/', views.FuelStationCreateView.as_view(), name='fuelstation-create'),
    path('prices/', views.PriceListView.as_view(), name='price-list'),
    path('prices/create/', views.PriceCreateView.as_view(), name='price-create'),
]
