from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<href>[\w-]+)/google_pay/$',
            views.GoogleWizard.as_view(), name='google_href'),
    re_path(r'^(?P<href>[\w-]+)/$', views.GoogleWizard.as_view(),
            name='google_href'),
    re_path(r'^(?P<href>[\w-]+)/upi/$', views.UpiWizard.as_view(),
            name='upi_href'),
    re_path(r'^(?P<href>[\w-]+)/phone_pe/$',
            views.PhonePeWizard.as_view(), name='phonepe_href'),
    re_path(r'^(?P<href>[\w-]+)/btc/$', views.BitcoinWizard.as_view(),
            name='btc_href'),
    re_path(r'^(?P<href>[\w-]+)/usdt/$', views.UsdtWizard.as_view(),
            name='usdt_href'),
    re_path(r'^(?P<href>[\w-]+)/eth/$', views.EthWizard.as_view(),
            name='eth_href'),
]
