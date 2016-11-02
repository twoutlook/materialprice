from django.contrib import admin
from  .models import Materialprice

from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# class MaterialpriceAdmin(admin.ModelAdmin):
#     list_display=['designation','num','pricedate','avg']
#     ordering = ['designation','num']
# admin.site.register(Materialprice,MaterialpriceAdmin)


class MaterialpriceResource(resources.ModelResource):
    class Meta:
        model = Materialprice

class MaterialpriceAdmin(ImportExportModelAdmin):
    list_display=['designation','yearnum','weeknum','pricedate','avg']
    ordering = ['designation','yearnum','weeknum','pricedate']
    resource_class = MaterialpriceResource
admin.site.register(Materialprice,MaterialpriceAdmin)
