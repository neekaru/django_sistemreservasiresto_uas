from django.shortcuts import render
from .models import Reservasi, Meja, Pelanggan, Pembayaran
from django.db.models import Count, Sum
# Create your views here.

def daftar_reservasi(request):
    reservasi_list = Reservasi.objects.all().order_by('waktu_reservasi')
    for r in reservasi_list:
        r.waktu_reservasi = r.waktu_reservasi.strftime("%H:%M")
    return render(request, 'reservasi/index.html', {'reservasi_list': reservasi_list})

