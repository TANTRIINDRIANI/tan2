from pickle import TRUE
from django.db import models

# Create your models here.
class BELAH_KETUPAT(models.Model):
    NO=models.CharField(max_length=50)
    NAMA=models.CharField(max_length=40)
    GAMBAR=models.CharField(max_length=40)
    PENGERTIAN=models.CharField(max_length=40)
    CIRI_CIRI=models.CharField(max_length=40)
    RUMUS_LUAS=models.CharField(max_length=40)
    RUMUS_KELILING=models.CharField(max_length=40)

    def _str_(self):
        return self.NO