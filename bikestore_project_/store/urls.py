from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.bike_list, name='bike_list'),
    path('bike/<slug:slug>/', views.bike_detail, name='bike_detail'),
]
