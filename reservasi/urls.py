from django.urls import path
from . import views

urlpatterns = [
    # Root path for showing reservations
    path('', views.daftar_reservasi, name='daftar_reservasi'),  # This will handle the root URL
    path('reservasi/', views.daftar_reservasi, name='daftar_reservasi_alt'),  # Keep this as an alternative path
]