from django.db import models

# Create your models here.
class Meja(models.Model):
    class Meta:
        verbose_name = 'Meja'
        verbose_name_plural = 'Meja'

    nomor_meja = models.CharField(max_length=10)
    jumlah_kursi = models.IntegerField()
    status_meja = models.CharField(max_length=20, choices=[('tersedia', 'Tersedia'), ('dipesan', 'Dipesan'), ('digunakan', 'Digunakan')])
    jenis_meja = models.CharField(max_length=20, choices=[('reguler', 'Reguler'), ('VIP', 'VIP'), ('outdoor', 'Outdoor')])

    def __str__(self):
        return f"Meja {self.nomor_meja}"

class Pelanggan(models.Model):
    class Meta:
        verbose_name = 'Pelanggan'
        verbose_name_plural = 'Pelanggan'

    nama = models.CharField(max_length=100)
    email = models.EmailField()
    nomor_telepon = models.CharField(max_length=20)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Reservasi(models.Model):
    class Meta:
        verbose_name = 'Reservasi'
        verbose_name_plural = 'Reservasi'

    meja = models.ForeignKey(Meja, on_delete=models.CASCADE)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    tanggal_reservasi = models.DateField()
    waktu_reservasi = models.TimeField()
    jumlah_orang = models.IntegerField()
    status_reservasi = models.CharField(max_length=20, choices=[('Diterima', 'Diterima'), ('Dibatalkan', 'Dibatalkan'), ('Selesai', 'Selesai'), ('Ditunda', 'Ditunda')])

    def __str__(self):
        return f"Reservasi {self.id} - {self.pelanggan.nama}"

class Pembayaran(models.Model):
    class Meta:
        verbose_name = 'Pembayaran'
        verbose_name_plural = 'Pembayaran'

    reservasi = models.ForeignKey(Reservasi, on_delete=models.CASCADE)
    jumlah_pembayaran = models.DecimalField(max_digits=10, decimal_places=2)
    metode_pembayaran = models.CharField(max_length=20, choices=[('Kartu Kredit', 'Kartu Kredit'), ('Tunai', 'Tunai'), ('Transfer Bank', 'Transfer Bank')])
    status_pembayaran = models.CharField(max_length=20, choices=[('Belum Dibayar', 'Belum Dibayar'), ('Dibayar', 'Dibayar'), ('Gagal', 'Gagal')])

    def __str__(self):
        return f"Pembayaran {self.id} - {self.reservasi.id}"
