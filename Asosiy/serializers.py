from rest_framework import serializers
from .models import *


class SuvSerializers(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'


class MijozSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'


class AdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class HaydovchiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'


class BuyurtmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'


