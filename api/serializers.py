from main import models
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fuel
        fields = '__all__'



class FuelStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FuelStation
        fields = '__all__'


class FuelStationSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = models.FuelStation
        fields = ['name', 'description', 'category', 'image', 'avaliable_fuels', 'opening_time', 'closing_time', 'price']


class FuelStationSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.FuelStation
        fields = ['name', 'category', 'image',]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = '__all__'