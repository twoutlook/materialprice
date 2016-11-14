from django.shortcuts import render

# 公司现开通上海有色网会员，本次有效期为一年。
#    网站：www.smm.cn       帐户：fulltech        密码：skyrock

'''
3#：良好的流动性和机械性能。应用于对机械强度要求不高的铸件，如玩具、灯具、装饰品、部分电器件。
5#：良好的流动性和好的机械性能。应用于对机械强度有一定要求的铸件，如汽车配件、机电配件、机械零件、电器元件。
总的来说，3号比5号要软一点。
'''

# PART 1 OF 2
from .models import Materialprice
from .models import Purchaseorder
from .models import Receiving
from django.db.models import Count, Min, Sum, Avg

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
