from rest_framework import serializers
from .models import Katigoriya, Mahsulot


class KatigoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Katigoriya
        fields = '__all__'


class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = '__all__'
