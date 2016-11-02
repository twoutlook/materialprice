from django.contrib import admin

# Register your models here.
from .models import Report
from .models import Employee
from .models import Vacation
from .models import Mailbox



# only show def __str__(self):
# admin.site.register(TaichiStyle)
# admin.site.register(TaichiSet)
# admin.site.register(TaichiMove)

# to show selected fields
class ReportAdmin(admin.ModelAdmin):
    list_display=['reportdate','reportnum','description']
    ordering = ['reportdate','reportnum',]
admin.site.register(Report,ReportAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['firstdate','fullname']
    ordering = ['firstdate','fullname',]
admin.site.register(Employee,EmployeeAdmin)

class VacationAdmin(admin.ModelAdmin):
    list_display=['fullname','vacationnum','vacationfrom','vacationto','vacationstatus']
    ordering = ['fullname','vacationnum','vacationfrom','vacationto']
admin.site.register(Vacation,VacationAdmin)

class MailboxAdmin(admin.ModelAdmin):
    list_display=['fullname','mailbox1','mailbox2','mailbox3','mailbox4',]
    ordering = ['mailbox1']
admin.site.register(Mailbox,MailboxAdmin)
