from django.shortcuts import render

# 公司现开通上海有色网会员，本次有效期为一年。
#    网站：www.smm.cn       帐户：fulltech        密码：skyrock

'''
3#：良好的流动性和机械性能。应用于对机械强度要求不高的铸件，如玩具、灯具、装饰品、部分电器件。
5#：良好的流动性和好的机械性能。应用于对机械强度有一定要求的铸件，如汽车配件、机电配件、机械零件、电器元件。
总的来说，3号比5号要软一点。
'''

from django.db.models import Count, Min, Sum, Avg

# PART 1 OF 2
from .models import Materialprice
from .models import Purchaseorder
from .models import Receiving
from .models import Smm

# PART 2 OF 2
# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Materialprice.objects.order_by('designation', 'id')[:3000]
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'Material Price','item_list': item_list}
    return render(request, 'materialprice/index.html', context)

def po(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Purchaseorder.objects.order_by('vendor', 'podate', 'part')[:3000]
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'Material Price','item_list': item_list}
    return render(request, 'materialprice/po.html', context)
def receiving(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Receiving.objects.order_by('FO', 'FC', 'FE', 'FF')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Receiving.objects.values('FO','FC','FE').annotate(sumFI=Sum('FI'), avgFJ=Avg('FJ'),sumFL=Sum('FL'),avgMo=Sum('FL')/Sum('FI'),countFG=Count('FG'))
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'RR','item_list': item_list,'subtotal': subtotal}
    return render(request, 'materialprice/receiving.html', context)


# designation = models.CharField(max_length=32,verbose_name="牌号")
# pricedate = models.CharField(max_length=10,verbose_name="行情日期")
# priceavg = models.DecimalField(max_digits=9, decimal_places=2,verbose_name="平均价")
# yearnum = models.IntegerField(default=0, verbose_name="年")
# monthnum = models.IntegerField(default=0, verbose_name="月")
# quarternum = models.IntegerFiel
def smm(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'materialprice/smm.html', context)



item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
avgbymonth=Smm.objects.values('yearnum','monthnum','designation').annotate(avg=Avg('priceavg')/1000)
bymonthcheck=Smm.objects.values('yearnum','monthnum','designation').annotate(cnt=Count('designation'))
byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)

  
def step0(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'STEP 0','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'materialprice/step0.html', context)
def step1(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    # item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    # subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'bymonth': bymonth,'bymonthcheck': bymonthcheck}
    return render(request, 'materialprice/step1.html', context)

def bymonth(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    # item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    # subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'avgbymonth': avgbymonth,'bymonthcheck': bymonthcheck}
    return render(request, 'materialprice/bymonth.html', context)


def step2(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'materialprice/step2.html', context)
def step3(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'materialprice/step3.html', context)
