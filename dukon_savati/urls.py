from django.urls import path
from .views import MahsulotDetailView, MahsulotListView

urlpatterns = [
    path('mahsulotlar/', MahsulotListView.as_view(), name='mahsulotlar_list'),
    path('mahsulot/<uuid:pk>/', MahsulotDetailView.as_view(), name='mahsulot_detail')
]