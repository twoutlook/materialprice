from django.db import models

# Create your models here.
class Report(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    reportdate = models.DateField(verbose_name="回報日期")
    reportnum = models.IntegerField(default=0, verbose_name="項次")
    description = models.CharField(max_length=500,verbose_name="說明")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "回報"
        verbose_name_plural = "回報"

class Employee(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    fullname = models.CharField(verbose_name="員工姓名",max_length=32)
    firstdate = models.DateField(verbose_name="報到日期")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.fullname
    class Meta:
        verbose_name = "員工"
        verbose_name_plural = "員工"

class Mailbox(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    fullname = models.CharField(verbose_name="員工姓名",max_length=32)
    mailbox1 = models.EmailField(max_length=254, blank=True, null=True,verbose_name="fulltech-metal.net")
    mailbox2 = models.EmailField(max_length=254, blank=True, null=True,verbose_name="skyrock-casting.org")
    mailbox3 = models.EmailField(max_length=254, blank=True, null=True,verbose_name="fulltech-metal.com")
    mailbox4 = models.EmailField(max_length=254, blank=True, null=True,verbose_name="skyrock-casting.com")

    remarks = models.CharField(max_length=200,verbose_name="備註")
    def __str__(self):
        return self.fullname
    class Meta:
        verbose_name = "郵箱"
        verbose_name_plural = "郵箱"


class Vacation(models.Model):
    STATUS_CHOICES = (

    ('報到日期', '報到日期'),
    ('已休假', '已休假'),
    ('申請休假', '申請休假'),
    )
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    fullname = models.ForeignKey( 'Employee', on_delete=models.CASCADE,verbose_name="員工姓名")
    vacationnum = models.IntegerField(default=1, verbose_name="第幾次")
    vacationfrom = models.DateField(verbose_name="起")
    vacationto = models.DateField(verbose_name="止")
    # vacationstatus = models.DateField(verbose_name="狀態")

    vacationstatus = models.CharField(default="申請休假",choices=STATUS_CHOICES,max_length=50,verbose_name="狀態")
#
    # description = models.CharField(max_length=500,verbose_name="說明")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return str(self.fullname)
    class Meta:
        verbose_name = "休假"
        verbose_name_plural = "休假"
