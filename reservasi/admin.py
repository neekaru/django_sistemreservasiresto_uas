from django.contrib import admin
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from datetime import timedelta  # Import timedelta function
from unfold.contrib.filters.admin import (
    FieldTextFilter,
    RangeDateFilter,
    SliderNumericFilter,
    RangeNumericFilter,
    RangeDateTimeFilter,
    RangeNumericListFilter,
)
from django.contrib.admin import SimpleListFilter
from .models import Meja, Pelanggan, Reservasi, Pembayaran

# Register your models here.

@admin.register(Meja)
class MejaAdmin(ModelAdmin):
    list_display = ["nomor_meja", "jumlah_kursi", "status_meja", "jenis_meja"]
    list_filter_submit = True
    list_filter = [
        ("nomor_meja", FieldTextFilter),
        ("status_meja", FieldTextFilter),
        ("jenis_meja", FieldTextFilter),
    ]
    ordering = ["nomor_meja"]
    search_fields = ["nomor_meja", "status_meja", "jenis_meja"]

@admin.register(Pelanggan)
class PelangganAdmin(ModelAdmin):
    list_display = ["nama", "email", "nomor_telepon", "alamat"]
    list_filter_submit = True
    list_filter = [
        ("nama", FieldTextFilter),
        ("email", FieldTextFilter),
        ("nomor_telepon", FieldTextFilter),
    ]
    ordering = ["nama"]
    search_fields = ["nama", "email", "nomor_telepon", "alamat"]

@admin.register(Reservasi) 
class ReservasiAdmin(ModelAdmin):
    list_display = ["meja", "pelanggan", "tanggal_reservasi", "waktu_reservasi", "jumlah_orang", "status_reservasi"]
    list_filter_submit = True
    list_filter = [
        ("meja", FieldTextFilter),
        ("pelanggan", FieldTextFilter),
        ("tanggal_reservasi", RangeDateFilter),
        ("status_reservasi", FieldTextFilter),
    ]
    ordering = ["tanggal_reservasi", "waktu_reservasi"]
    search_fields = ["meja__nomor_meja", "pelanggan__nama", "status_reservasi"]

@admin.register(Pembayaran)
class PembayaranAdmin(ModelAdmin):
    list_display = ["reservasi", "jumlah_pembayaran", "metode_pembayaran", "status_pembayaran"]
    list_filter_submit = True
    list_filter = [
        ("reservasi", FieldTextFilter),
        ("jumlah_pembayaran", RangeNumericFilter),
        ("metode_pembayaran", FieldTextFilter),
        ("status_pembayaran", FieldTextFilter),
    ]
    ordering = ["reservasi"]
    search_fields = ["reservasi__id", "metode_pembayaran", "status_pembayaran"]