from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
#     path('withdrawal/',
#          views.withdrawal_choose_payment, name='choose_withdrawal'),
    path('withdrawal_google_pay/',
         login_required(views.WithdrawalGoogleWizard.as_view()),
         name='google_withdrawal'),
    path('withdrawal_upi/', login_required(
         views.WithdrawalUpiWizard.as_view()), name='upi_withdrawal'),
    path('withdrawal_phonepe/',
         login_required(views.WithdrawalPhonePeWizard.as_view()),
         name='phonepe_withdrawal'),
    path('withdrawal_btc/', login_required(
         views.WithdrawalBtcWizard.as_view()), name='btc_withdrawal'),
    path('withdrawal_usdt/', login_required(
         views.WithdrawalUsdtWizard.as_view()), name='usdt_withdrawal'),
    path('withdrawal_eth/', login_required(
         views.WithdrawalEthWizard.as_view()), name='eth_withdrawal'),
]
