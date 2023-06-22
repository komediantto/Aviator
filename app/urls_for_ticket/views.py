from django.shortcuts import redirect

from crediting_money import forms
from crediting_money.models import PaymentRequest
from .models import TempAcc
from crediting_money import models
import requests
from formtools.wizard.views import SessionWizardView


FORMS = [('form1', forms.PaymentRequestForm1),
         ('form2', forms.PaymentRequestForm2)]

TEMPLATES = {
    'form1': 'temp_payment/deposit.html',
    'form2': 'payment/secondform.html'
}


# def start(request):
#     href = request.path.split('/')
#     context = {'start': f'/tempacc/{href[2]}/choose_payment/'}
#     return render(request,
#                   'temp_payment/start_button_href.html', context=context)


# def choose_payment(request):
#     href = request.path.split('/')
#     context = {'google': f'/tempacc/{href[2]}/google_pay/',
#                'upi': f'/tempacc/{href[2]}/upi/',
#                'phonepe': f'/tempacc/{href[2]}/phonepe/',
#                'btc': f'/tempacc/{href[2]}/btc/',
#                'usdt': f'/tempacc/{href[2]}/usdt/',
#                'eth': f'/tempacc/{href[2]}/eth/',
#                }
#     return render(request,
#                   'temp_payment/choose_payment_href.html', context=context)


# def google(request, href):
#     logging.info(request.META)
#     google = models.Google.objects.first()
#     form = forms.PaymentRequestForm(request.POST or None)
#     obj = TempAcc.objects.get(clean_url=href)
#     if form.is_valid():
#         payment_system = PaymentRequest()
#         payment_system.payment_system = 'Google Pay'
#         ticket = form.save(commit=False)
#         if ticket.amount < 10000 or ticket.amount > 50000:
#             context = {
#                 'form': form,
#                 'system': 'Номер карты',
#                 'data': google,
#                 'text': 'Send money to the our card by Google Pay. Enter amount and click on PAY.',
#                 'name': 'Google Pay',
#                 'balance': obj.balance,
#                 'href': href
#             }
#             context['message'] = True
#             return render(request, "temp_payment/deposit.html", context)
#         ticket.href = obj
#         ticket.payment_system = payment_system.payment_system
#         ticket.save()
#         return redirect(f'/tempacc/{obj}')

#     context = {
#         'form': form,
#         'system': 'Card number',
#         'data': google,
#         'text': 'Send money to the our card by Google Pay. Enter amount and click on PAY.',
#         'name': 'Google Pay',
#         'balance': obj.balance,
#         'href': href
#     }

#     return render(request, "temp_payment/deposit.html", context)


class GoogleWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'temp_payment/deposit.html'

    def done(self, form_list, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'Google Pay'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.href = obj
        ticket.save()
        return redirect(f'/tempacc/{obj}')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        google = models.Google.objects.first()
        context = super(GoogleWizard, self).get_context_data(**kwargs) | {
            'system': 'Card number',
            'data': google,
            'text': 'Send money to the our card by Google Pay. Enter amount and click on PAY.',
            'name': 'Google Pay',
            'balance': obj.balance,
            'href': self.kwargs.get('href')
        }
        return context


# def upi(request, href):
#     upi = models.Upi.objects.first()
#     form = forms.PaymentRequestForm(request.POST or None)
#     obj = TempAcc.objects.get(clean_url=href)
#     if form.is_valid():
#         payment_system = PaymentRequest()
#         payment_system.payment_system = 'UPI'
#         ticket = form.save(commit=False)
#         if ticket.amount < 10000 or ticket.amount > 50000:
#             context = {
#                 'form': form,
#                 'system': 'UPI ID',
#                 'data': upi,
#                 'text': 'Send money to the our UPI ID. Enter amount and click on PAY.',
#                 'name': 'UPI',
#                 'balance': obj.balance,
#                 'href': href
#             }
#             context['message'] = True
#             return render(request, "temp_payment/deposit.html", context)
#         ticket.href = obj
#         ticket.payment_system = payment_system.payment_system
#         ticket.save()
#         return redirect(f'/tempacc/{obj}')

#     context = {
#         'form': form,
#         'system': 'UPI ID',
#         'data': upi,
#         'text': 'Send money to the our UPI ID. Enter amount and click on PAY.',
#         'name': 'UPI',
#         'balance': obj.balance,
#         'href': href
#     }
#     return render(request, "temp_payment/deposit.html", context)


class UpiWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'temp_payment/deposit.html'

    def done(self, form_list, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'UPI'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.href = obj
        ticket.save()
        return redirect(f'/tempacc/{obj}')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        upi = models.Upi.objects.first()
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        context = super(UpiWizard, self).get_context_data(**kwargs) | {
            'system': 'UPI ID',
            'data': upi,
            'text': 'Send money to the our UPI ID. Enter amount and click on PAY.',
            'name': 'UPI',
            'balance': obj.balance,
            'href': self.kwargs.get('href')
        }
        return context


# def phonepe(request, href):
#     logging.info(href)
#     phonepe = models.PhonePe.objects.first()
#     form = forms.PaymentRequestForm(request.POST or None)
#     obj = TempAcc.objects.get(clean_url=href)
#     if form.is_valid():
#         payment_system = PaymentRequest()
#         payment_system.payment_system = 'PhonePe'
#         ticket = form.save(commit=False)
#         if ticket.amount < 10000 or ticket.amount > 50000:
#             context = {
#                 'form': form,
#                 'system': 'Phone number',
#                 'data': phonepe,
#                 'text': 'Send money to the our Phone Pe number. Enter amount and click on PAY.',
#                 'name': 'Phone Pe',
#                 'balance': obj.balance,
#                 'href': href
#             }
#             context['message'] = True
#             return render(request, "temp_payment/deposit.html", context)
#         ticket.href = obj
#         ticket.payment_system = payment_system.payment_system
#         ticket.save()
#         return redirect(f'/tempacc/{obj}')

#     context = {
#         'form': form,
#         'system': 'Phone number',
#         'data': phonepe,
#         'text': 'Send money to the our Phone Pe number. Enter amount and click on PAY.',
#         'name': 'Phone Pe',
#         'balance': obj.balance,
#         'href': href
#     }
#     return render(request, "temp_payment/deposit.html", context)


class PhonePeWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'temp_payment/deposit.html'

    def done(self, form_list, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'Phone Pe'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.href = obj
        ticket.save()
        return redirect(f'/tempacc/{obj}')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        phonepe = models.PhonePe.objects.first()
        context = super(PhonePeWizard, self).get_context_data(**kwargs) | {
            'system': 'Phone number',
            'data': phonepe,
            'text': 'Send money to the our Phone Pe number. Enter amount and click on PAY.',
            'name': 'Phone Pe',
            'balance': obj.balance,
            'href': self.kwargs.get('href')
        }
        return context


# def usdt(request, href):
#     usdt = models.Usdt.objects.first()
#     form = forms.PaymentRequestForm(request.POST or None)
#     obj = TempAcc.objects.get(clean_url=href)
#     if form.is_valid():
#         payment_system = PaymentRequest()
#         payment_system.payment_system = 'USDT'
#         ticket = form.save(commit=False)
#         response = requests.get(
#             'https://min-api.cryptocompare.com/data/price?fsym=USDT&tsyms=RUB')
#         exchange = response.json()['RUB']
#         rub = float(ticket.amount)*float(exchange)
#         if rub < 10000 or rub > 50000:
#             context = {
#                 'form': form,
#                 'system': 'USDT wallet address',
#                 'data': usdt,
#                 'text': 'Send money to the our USDT wallet. Enter amount and click on PAY.',
#                 'name': 'USDT',
#                 'balance': obj.balance,
#                 'href': href
#             }
#             context['message'] = True
#             return render(request, "temp_payment/deposit.html", context)
#         ticket.href = obj
#         ticket.payment_system = payment_system.payment_system
#         ticket.save()
#         return redirect(f'/tempacc/{obj}')

#     context = {
#         'form': form,
#         'system': 'USDT wallet address',
#         'data': usdt,
#         'text': 'Send money to the our USDT wallet. Enter amount and click on PAY.',
#         'name': 'USDT',
#         'balance': obj.balance,
#         'href': href
#     }
#     return render(request, "temp_payment/deposit.html", context)


class UsdtWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'temp_payment/deposit.html'

    def done(self, form_list, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'USDT'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.href = obj
        ticket.save()
        return redirect(f'/tempacc/{obj}')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        usdt = models.Usdt.objects.first()
        context = super(UsdtWizard, self).get_context_data(**kwargs) | {
            'system': 'USDT wallet address',
            'data': usdt,
            'text': 'Send money to the our USDT wallet. Enter amount and click on PAY.',
            'name': 'USDT',
            'balance': obj.balance,
            'href': self.kwargs.get('href')
        }
        return context


# def eth(request, href):
#     eth = models.Eth.objects.first()
#     form = forms.PaymentRequestForm(request.POST or None)
#     obj = TempAcc.objects.get(clean_url=href)
#     if form.is_valid():
#         payment_system = PaymentRequest()
#         payment_system.payment_system = 'ETH'
#         ticket = form.save(commit=False)
#         response = requests.get(
#             'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=RUB')
#         exchange = response.json()['RUB']
#         rub = float(ticket.amount)*float(exchange)
#         if rub < 10000 or rub > 50000:
#             context = {
#                 'form': form,
#                 'system': 'ETH wallet address',
#                 'data': eth,
#                 'text': 'Send money to the our ETH wallet. Enter amount and click on PAY.',
#                 'name': 'Ethereum',
#                 'balance': obj.balance,
#                 'href': href
#             }
#             context['message'] = True
#             return render(request, "temp_payment/deposit.html", context)
#         ticket.href = obj
#         ticket.payment_system = payment_system.payment_system
#         ticket.save()
#         return redirect(f'/tempacc/{obj}')

#     context = {
#         'form': form,
#         'system': 'ETH wallet address',
#         'data': eth,
#         'text': 'Send money to the our ETH wallet. Enter amount and click on PAY.',
#         'name': 'Ethereum',
#         'balance': obj.balance,
#         'href': href
#     }
#     return render(request, "temp_payment/deposit.html", context)


class EthWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'temp_payment/deposit.html'

    def done(self, form_list, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'ETH'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.href = obj
        ticket.save()
        return redirect(f'/tempacc/{obj}')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        eth = models.Eth.objects.first()
        context = super(EthWizard, self).get_context_data(**kwargs) | {
            'system': 'ETH wallet address',
            'data': eth,
            'text': 'Send money to the our ETH wallet. Enter amount and click on PAY.',
            'name': 'Ethereum',
            'balance': obj.balance,
            'href': self.kwargs.get('href')
        }
        return context


# def btc(request, href):
#     btc = models.Btc.objects.first()
#     form = forms.PaymentRequestForm(request.POST or None)
#     obj = TempAcc.objects.get(clean_url=href)
#     if form.is_valid():
#         payment_system = PaymentRequest()
#         payment_system.payment_system = 'BTC'
#         ticket = form.save(commit=False)
#         response = requests.get('https://blockchain.info/ticker')
#         exchange = response.json()['RUB']['last']
#         rub = float(ticket.amount)*float(exchange)

#         if rub < 10000 or rub > 50000:
#             context = {
#                 'form': form,
#                 'system': 'BTC wallet address',
#                 'data': btc,
#                 'text': 'Send money to the our BTC wallet. Enter amount and click on PAY.',
#                 'name': 'Bitcoin',
#                 'balance': obj.balance,
#                 'href': href
#             }
#             context['message'] = True
#             return render(request, "temp_payment/deposit.html", context)
#         ticket.href = obj
#         ticket.payment_system = payment_system.payment_system
#         ticket.save()
#         return redirect(f'/tempacc/{obj}')

#     context = {
#         'form': form,
#         'system': 'BTC wallet address',
#         'data': btc,
#         'text': 'Send money to the our BTC wallet. Enter amount and click on PAY.',
#         'name': 'Bitcoin',
#         'balance': obj.balance,
#         'href': href
#     }
#     return render(request, "temp_payment/deposit.html", context)


class BitcoinWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'temp_payment/deposit.html'

    def done(self, form_list, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'BTC'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.href = obj
        ticket.save()
        return redirect(f'/tempacc/{obj}')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        obj = TempAcc.objects.get(clean_url=self.kwargs.get('href'))
        btc = models.Btc.objects.first()
        context = super(BitcoinWizard, self).get_context_data(**kwargs) | {
            'system': 'BTC wallet address',
            'data': btc,
            'text': 'Send money to the our BTC wallet. Enter amount and click on PAY.',
            'name': 'Bitcoin',
            'balance': obj.balance,
            'href': self.kwargs.get('href')
        }
        return context
