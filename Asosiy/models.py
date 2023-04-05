from django.db import models
from django.contrib.auth.models import User



class Suv(models.Model):
    brend = models.CharField(max_length=30)
    narx = models.IntegerField()
    litr = models.CharField(max_length=10)
    batafsil = models.CharField(max_length=50)
    def __int__(self):
        return self.brend

class Mijoz(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    manzil = models.CharField(max_length=50)
    qarz = models.IntegerField()
    def __int__(self):
        return self.ism

class Admin(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    ish_vaqti = models.DateTimeField()
    def __int__(self):
        return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    kiritilgan_sana = models.DateTimeField()
    def __int__(self):
        return self.ism

class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv,on_delete=models.CASCADE,null=True)
    buyurtma_vaqti = models.DateTimeField()
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE,null=True)
    buyurtma_miqdori = models.SmallIntegerField()
    umumiy_summa = models.IntegerField()
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE,null=True)
    haydovchi = models.ForeignKey(Haydovchi,on_delete=models.CASCADE,null=True)
    def __int__(self):
        return self.buyurtma_miqdori




