from django.db import models

# Create your models here.
class Materialprice(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    designation = models.CharField(max_length=32,verbose_name="牌号")
    yearnum = models.IntegerField(default=0, verbose_name="年")
    weeknum = models.IntegerField(default=0, verbose_name="周")
    pricedate = models.CharField(max_length=10,verbose_name="行情日期")
    avg = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="平均价")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.designation
    class Meta:
        verbose_name = "材料價格"
        verbose_name_plural = "材料價格"
