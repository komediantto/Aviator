from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.GoogleWizard.as_view()), name='google'),
    path('google_pay/', login_required(views.GoogleWizard.as_view()),
         name='google'),
    path('upi/', login_required(views.UpiWizard.as_view()), name='upi'),
    path('phonepe/', login_required(views.PhonePeWizard.as_view()),
         name='phonepe'),
    path('btc/', login_required(views.BitcoinWizard.as_view()), name='btc'),
    path('usdt/', login_required(views.UsdtWizard.as_view()), name='usdt'),
    path('eth/', login_required(views.EthWizard.as_view()), name='eth'),
]
