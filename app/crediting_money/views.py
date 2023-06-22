from django.shortcuts import redirect

from .forms import PaymentRequestForm1, PaymentRequestForm2


from .models import Google, Upi, Btc, Usdt, PhonePe, Eth, PaymentRequest
import requests
from formtools.wizard.views import SessionWizardView


FORMS = [('form1', PaymentRequestForm1),
         ('form2', PaymentRequestForm2)]

TEMPLATES = {
    'form1': 'payment/index.html',
    'form2': 'payment/secondform.html'
}


# @login_required
# def start(request):
#     context = {'user': request.user}
#     return render(request, 'payment/index.html', context=context)


# @login_required
# def choose_payment(request):
#     return render(request, 'payment/choose_payment.html')


# @login_required
# def google(request):
#     google = Google.objects.first()
#     form = PaymentRequestForm(request.POST or None)

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
#                 'name': 'Google Pay'
#             }
#             context['message'] = True
#             return render(request, "payment/index.html", context)
#         ticket.payment_system = payment_system.payment_system
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'Card number',
#         'data': google,
#         'text': 'Send money to the our card by Google Pay. Enter amount and click on PAY.',
#         'name': 'Google Pay',
#     }
#     return render(request, "payment/index.html", context=context)


class GoogleWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'payment/index.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest(payment_system='Google Pay',
                                amount=form_data[0]['amount'],
                                transaction_id=form_data[1]['transaction_id'],
                                user=self.request.user)
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        google = Google.objects.first()
        context = super(GoogleWizard, self).get_context_data(**kwargs) | {
            'system': 'Card number',
            'data': google,
            'text': 'Send money to the our card by Google Pay. Enter amount and click on PAY.',
            'name': 'Google Pay',
        }
        return context


# @login_required
# def upi(request):
#     upi = Upi.objects.first()
#     form = PaymentRequestForm1(request.POST or None)

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
#                 'name': 'UPI'
#             }
#             context['message'] = True
#             return render(request, "payment/index.html", context)
#         ticket.payment_system = payment_system.payment_system
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#             'form': form,
#             'system': 'UPI ID',
#             'data': upi,
#             'text': 'Send money to the our UPI ID. Enter amount and click on PAY.',
#             'name': 'UPI'
#         }
#     return render(request, "payment/index.html", context)


class UpiWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'payment/index.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'UPI'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.user = self.request.user
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        upi = Upi.objects.first()
        context = super(UpiWizard, self).get_context_data(**kwargs) | {
            'system': 'UPI ID',
            'data': upi,
            'text': 'Send money to the our UPI ID. Enter amount and click on PAY.',
            'name': 'UPI',
        }
        return context


# @login_required
# def phonepe(request):
#     phonepe = PhonePe.objects.first()
#     form = PaymentRequestForm1(request.POST or None)

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
#                 'name': 'Phone Pe'
#             }
#             context['message'] = True
#             return render(request, "payment/index.html", context)
#         ticket.payment_system = payment_system.payment_system
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'Phone number',
#         'data': phonepe,
#         'text': 'Send money to the our Phone Pe number. Enter amount and click on PAY.',
#         'name': 'Phone Pe'
#     }
#     return render(request, "payment/index.html", context)


class PhonePeWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'payment/index.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'Phone Pe'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.user = self.request.user
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        phonepe = PhonePe.objects.first()
        context = super(PhonePeWizard, self).get_context_data(**kwargs) | {
            'system': 'Phone number',
            'data': phonepe,
            'text': 'Send money to the our Phone Pe number. Enter amount and click on PAY.',
            'name': 'Phone Pe',
        }
        return context


# @login_required
# def btc(request):
#     btc = Btc.objects.first()
#     form = PaymentRequestForm1(request.POST or None)

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
#                 'name': 'Bitcoin'
#             }
#             context['message'] = True
#             return render(request, "payment/index.html", context)
#         ticket.payment_system = payment_system.payment_system
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'BTC wallet address',
#         'data': btc,
#         'text': 'Send money to the our BTC wallet. Enter amount and click on PAY.',
#         'name': 'Bitcoin'
#     }
#     return render(request, "payment/index.html", context)


class BitcoinWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'payment/index.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'BTC'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.user = self.request.user
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        btc = Btc.objects.first()
        context = super(BitcoinWizard, self).get_context_data(**kwargs) | {
            'system': 'BTC wallet address',
            'data': btc,
            'text': 'Send money to the our BTC wallet. Enter amount and click on PAY.',
            'name': 'Bitcoin',
        }
        return context


# @login_required
# def usdt(request):
#     usdt = Usdt.objects.first()
#     form = PaymentRequestForm1(request.POST or None)

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
#                 'name': 'USDT'
#             }
#             context['message'] = True
#             return render(request, "payment/index.html", context)
#         ticket.payment_system = payment_system.payment_system
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'USDT wallet address',
#         'data': usdt,
#         'text': 'Send money to the our USDT wallet. Enter amount and click on PAY.',
#         'name': 'USDT'
#     }
#     return render(request, "payment/index.html", context)


class UsdtWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'payment/index.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'USDT'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.user = self.request.user
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        usdt = Usdt.objects.first()
        context = super(UsdtWizard, self).get_context_data(**kwargs) | {
            'system': 'USDT wallet address',
            'data': usdt,
            'text': 'Send money to the our USDT wallet. Enter amount and click on PAY.',
            'name': 'USDT',
        }
        return context


# @login_required
# def eth(request):
#     eth = Eth.objects.first()

#     form = PaymentRequestForm1(request.POST or None)
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
#                 'name': 'Ethereum'
#             }
#             context['message'] = True
#             return render(request, "payment/index.html", context)
#         ticket.payment_system = payment_system.payment_system
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'ETH wallet address',
#         'data': eth,
#         'text': 'Send money to the our ETH wallet. Enter amount and click on PAY.',
#         'name': 'Ethereum'
#     }
#     return render(request, "payment/index.html", context)


class EthWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'payment/index.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = PaymentRequest()
        ticket.payment_system = 'ETH'
        ticket.amount = form_data[0]['amount']
        ticket.transaction_id = form_data[1]['transaction_id']
        ticket.user = self.request.user
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        eth = Eth.objects.first()
        context = super(EthWizard, self).get_context_data(**kwargs) | {
            'system': 'ETH wallet address',
            'data': eth,
            'text': 'Send money to the our ETH wallet. Enter amount and click on PAY.',
            'name': 'Ethereum',
        }
        return context
