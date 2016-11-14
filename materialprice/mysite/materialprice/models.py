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

# http://www.smm.cn/
# SMM 上海MM
class Smm(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    designation = models.CharField(max_length=32,verbose_name="牌号")
    pricedate = models.CharField(max_length=10,verbose_name="行情日期")
    priceavg = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="平均价")
    yearnum = models.IntegerField(default=0, verbose_name="年")
    monthnum = models.IntegerField(default=0, verbose_name="月")
    quarternum = models.IntegerField(default=0, verbose_name="季")

    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.designation
    class Meta:
        verbose_name = "上海有色網"
        verbose_name_plural = "上海有色網"

class Purchaseorder(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    vendor = models.CharField(max_length=32,verbose_name="厂商")
    part = models.CharField(max_length=128,verbose_name="品名")
    spec = models.CharField(max_length=128,verbose_name="规格")
    qty = models.IntegerField(default=0, verbose_name="数量")
    unit = models.CharField(default="KG",max_length=32,verbose_name="单位")
    price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="单价")
    podate = models.DateField(verbose_name="订单日期")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.vendor+"|"+self.part+"|"+str(self.qty)+str(self.podate)
    class Meta:
        verbose_name = "採購"
        verbose_name_plural = "採購"

class Receiving(models.Model):
    # A 01 序号
    # B 02 供应商
    # C 03 业务伙伴
    # D 04 物料代码
    # E 05 品名
    # F 06 进料日期
    # G 07 收料单号
    # H 08 单位
    # I 09 收货数量
    # J 10 含税单价
    # K 11 未税单价
    # L 12 未税金额
    # M 13 含税金额
    # N 14 类别
    # O 15 年月份

    # num = models.IntegerField(default=0,verbose_name="第幾式")
    FB = models.CharField(max_length=32,verbose_name="供应商")
    FC = models.CharField(max_length=32,verbose_name="业务伙伴")
    FD = models.CharField(max_length=64,verbose_name="物料代码")
    FE = models.CharField(max_length=64,verbose_name="品名")
    FF = models.DateField(verbose_name="进料日期")
    FG = models.CharField(max_length=64,verbose_name="收料单号")
    FH = models.CharField(default="KG",max_length=32,verbose_name="单位")
    FI = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="收货数量")
    FJ = models.DecimalField(max_digits=11, decimal_places=4,verbose_name="含税单价")
    FK = models.DecimalField(max_digits=11, decimal_places=4,verbose_name="未税单价")
    FL = models.DecimalField(max_digits=11, decimal_places=4,verbose_name="未税金额")
    FM = models.DecimalField(max_digits=11, decimal_places=4,verbose_name="含税金额")
    FN = models.CharField(default="原料类",max_length=32,verbose_name="类别")
    FO = models.CharField(default="2016-09",max_length=32,verbose_name="年月份")
    def __str__(self):
        return self.FC+"|"+self.FE
    class Meta:
        verbose_name = "進料表"
        verbose_name_plural = "進料表"
