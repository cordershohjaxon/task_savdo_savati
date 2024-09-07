from django.shortcuts import render
from rest_framework import generics
from .serializer import KatigoriyaSerializer, MahsulotSerializer
from .models import Mahsulot


class MahsulotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer


class MahsulotListView(generics.ListCreateAPIView):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        name = self.request.query_params.get('name')
        if category:
            queryset = queryset.filter(category__name__iexact=category)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset
