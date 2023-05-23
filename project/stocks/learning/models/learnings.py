from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='urun ismi')
    content = models.TextField(verbose_name='urun aciklamasi', max_length=500)
    created = models.DateTimeField(auto_now_add=True) #datetime aktif olarak guncellenir. 
    active = models.BooleanField(default=True)
    stock_count = models.BigIntegerField(verbose_name='stok_adedi') #burada bigintegerfield kullandim cunku girilecek sayinin degeri belli olmadigindan buyuk rakamlarda sorun yasamamak adina.
    price = models.DecimalField(verbose_name='urun fiyati', decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True) #adresleme icin kullanacagimdan unieq atadim. 


    class Meta:
        db_table = 'urunler'
        
    