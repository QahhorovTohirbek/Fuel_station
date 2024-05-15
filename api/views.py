from . import serializers
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from main import models


class CategoryCreateView(generics.CreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class FuelCreateView(generics.CreateAPIView):
    queryset = models.Fuel.objects.all()
    serializer_class = serializers.FuelSerializer


class FuelListView(generics.ListAPIView):
    queryset = models.Fuel.objects.all()
    serializer_class = serializers.FuelSerializer


class FuelStationCreateView(generics.CreateAPIView):
    queryset = models.FuelStation.objects.all()
    serializer_class = serializers.FuelStationSerializer


class FuelStationListView(generics.ListAPIView):
    queryset = models.FuelStation.objects.all()
    serializer_class = serializers.FuelStationSerializer


class PriceCreateView(generics.CreateAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializer


    
class PriceListView(generics.ListAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializer



