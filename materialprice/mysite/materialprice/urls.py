from django.conf.urls import url, include

from . import views

app_name = 'materialprice'
urlpatterns = [
    # url(r'^style19/$', views.style19, name='style19'),
    # url(r'^bydate/(?P<setnum>[0-9]+)/$', views.bydate, name='bydate'),
    # url(r'^vacation', views.vacation, name='vacation'),
    # url(r'^mailbox', views.mailbox, name='mailbox'),
    # url(r'^v2', views.indexv2, name='indexv2'),
    # url(r'^$', views.index, name='index'),
    url(r'^receiving', views.receiving, name='receiving'),
    url(r'^smm', views.smm, name='smm'),
    url(r'^step0', views.step0, name='step0'),
    url(r'^step1', views.step1, name='step1'),
    url(r'^step2', views.step2, name='step2'),
    url(r'^step3', views.step3, name='step3'),
    url(r'^po', views.po, name='po'),
    url(r'^', views.index, name='index'),

# url(r'^style19/(?P<setnum>[0-9]+)/(?P<movenum>[0-9]+)', views.style19detail2, name='style19detail2'),


]
