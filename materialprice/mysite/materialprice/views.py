from django.shortcuts import render
from .models import Materialprice
# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Materialprice.objects.order_by('designation', 'id')[:3000]
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'Material Price','item_list': item_list}
    return render(request, 'materialprice/index.html', context)

# Designation
# 名称；指定；称号；选定
# 网络命名；指示；牌号
