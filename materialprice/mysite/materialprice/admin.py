from django.contrib import admin


from import_export import resources
from import_export.admin import ImportExportModelAdmin


# PART 1 OF 3
from  .models import Materialprice
from  .models import Purchaseorder
from  .models import Receiving




# Register your models here.
# class MaterialpriceAdmin(admin.ModelAdmin):
#     list_display=['designation','num','pricedate','avg']
#     ordering = ['designation','num']
# admin.site.register(Materialprice,MaterialpriceAdmin)

# PART 2 OF 3
class MaterialpriceResource(resources.ModelResource):
    class Meta:
        model = Materialprice

class PurchaseorderResource(resources.ModelResource):
    class Meta:
        model = Purchaseorder
class ReceivingResource(resources.ModelResource):
    class Meta:
        model = Receiving

#
# PART 3 OF 3
class MaterialpriceAdmin(ImportExportModelAdmin):
    list_display=['designation','yearnum','weeknum','pricedate','avg']
    ordering = ['designation','yearnum','weeknum','pricedate']
    resource_class = MaterialpriceResource
admin.site.register(Materialprice,MaterialpriceAdmin)

class PurchaseorderAdmin(ImportExportModelAdmin):
    list_display=['vendor','podate','part','spec','qty','unit','price']
    ordering = ['vendor','podate','part']
    resource_class = PurchaseorderResource
admin.site.register(Purchaseorder,PurchaseorderAdmin)

class ReceivingAdmin(ImportExportModelAdmin):
    list_display=['FC','FE','FF','FH','FI','FJ','FG']
    ordering = ['FC','FE','FF']
    resource_class = ReceivingResource
admin.site.register(Receiving,ReceivingAdmin)


    #
    # vendor = models.CharField(max_length=32,verbose_name="厂商")
    # part = models.CharField(max_length=128,verbose_name="品名")
    # spec = models.CharField(max_length=128,verbose_name="规格")
    # qty = models.IntegerField(default=0, verbose_name="数量")
    # unit = models.CharField(max_length=32,verbose_name="单位")
    # price = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="单价")
    # podate = models.DateTimeField(max_length=10,verbose_name="订单日期")
