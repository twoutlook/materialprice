from django.shortcuts import render
from .models import Report
from .models import Employee
from .models import Vacation
from .models import Mailbox



from django.db.models import Count, Avg, Sum
# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = Report.objects.order_by('reportdate', 'reportnum')[:3000]
    context = {'current_user':request.user,'page_title':'Weekly Report','item_list': item_list}
    return render(request, 'weeklyreport/index.html', context)

def indexv2(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    subtotal=Report.objects.values('reportdate').annotate(rptcnt=Count('reportdate'))

    item_list = Report.objects.order_by('reportdate', 'reportnum')[:3000]
    context = {'current_user':request.user,'page_title':'Weekly Report V2','item_list': item_list,'subtotal':subtotal}
    return render(request, 'weeklyreport/indexv2.html', context)

def vacation(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # subtotal=Report.objects.values('reportdate').annotate(rptcnt=Count('reportdate'))
    name_list = Employee.objects.order_by('fullname', 'firstdate')[:3000]

    item_list = Vacation.objects.order_by('fullname', 'vacationnum')[:3000]
    context = {'current_user':request.user,'page_title':'休假','name_list': name_list,'item_list': item_list}
    return render(request, 'weeklyreport/vacation.html', context)

def mailbox(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # subtotal=Report.objects.values('reportdate').annotate(rptcnt=Count('reportdate'))
    # name_list = Employee.objects.order_by('fullname', 'firstdate')[:3000]

    item_list = Mailbox.objects.order_by('mailbox1')[:3000]
    context = {'current_user':request.user,'page_title':'MAILBOX','item_list': item_list}
    return render(request, 'weeklyreport/mailbox.html', context)

def bydate(request, bydate):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    item_list = TaichiMove.objects.filter(reportdate=bydate).order_by('reportnum')[:3000]
    context = {'current_user':request.user,'page_title':dydate,'item_list': item_list}
    return render(request, 'weeklyreport/bydate.html', context)
