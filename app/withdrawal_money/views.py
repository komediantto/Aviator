from django.shortcuts import render, redirect

from .forms import WithdrawalForm, WithdrawalForm2
from .models import WithdrawalRequest
from django.contrib.auth.decorators import login_required
from formtools.wizard.views import SessionWizardView


FORMS = [('form1', WithdrawalForm),
         ('form2', WithdrawalForm2)]


TEMPLATES = {
    'form1': 'withdrawal_money/withdraw.html',
    'form2': 'payment/secondform.html'
}

# @login_required
# def withdrawal_choose_payment(request):
#     return render(request, 'withdrawal_money/choose_withdrawal.html')


# @login_required
# def withdrawal_google(request):
#     form = WithdrawalGoogleForm(request.POST or None)
#     if form.is_valid():
#         ticket = form.save(commit=False)
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'Card number',
#         'name': 'Google Pay',
#     }
#     return render(request, "withdrawal_money/withdraw.html", context)


class WithdrawalGoogleWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'withdrawal_money/withdraw.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = WithdrawalRequest(payment_system='Google Pay',
                                   amount=form_data[0]['amount'],
                                   address=form_data[1]['address'],
                                   name=form_data[1]['name'],
                                   user=self.request.user)
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        context = super(WithdrawalGoogleWizard, self).get_context_data(**kwargs) | {
            'system': 'Card number',
            'name': 'Google Pay'
        }
        return context



# @login_required
# def withdrawal_upi(request):

#     form = WithdrawalUpiForm(request.POST or None)
#     if form.is_valid():
#         ticket = form.save(commit=False)
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'UPI ID',
#         'name': 'UPI'
#     }
#     return render(request, "withdrawal_money/withdraw.html", context)


class WithdrawalUpiWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'withdrawal_money/withdraw.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = WithdrawalRequest(payment_system='UPI',
                                   amount=form_data[0]['amount'],
                                   address=form_data[1]['address'],
                                   name=form_data[1]['name'],
                                   user=self.request.user)
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        context = super(WithdrawalUpiWizard, self).get_context_data(**kwargs) | {
            'system': 'UPI ID',
            'name': 'UPI'
        }
        return context


# @login_required
# def withdrawal_phonepe(request):

#     form = WithdrawalPhonePeForm(request.POST or None)
#     if form.is_valid():
#         ticket = form.save(commit=False)
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'Phone number',
#         'name': 'Phone Pe'
#     }
#     return render(request, "withdrawal_money/withdraw.html", context)


class WithdrawalPhonePeWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'withdrawal_money/withdraw.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = WithdrawalRequest(payment_system='Phone Pe',
                                   amount=form_data[0]['amount'],
                                   address=form_data[1]['address'],
                                   name=form_data[1]['name'],
                                   user=self.request.user)
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        context = super(WithdrawalPhonePeWizard, self).get_context_data(**kwargs) | {
            'system': 'Phone number',
            'name': 'Phone Pe'
        }
        return context


# @login_required
# def withdrawal_btc(request):

#     form = WithdrawalBtcForm(request.POST or None)
#     if form.is_valid():
#         ticket = form.save(commit=False)
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'BTC wallet address',
#         'name': 'Bitcoin'
#     }
#     return render(request, "withdrawal_money/withdraw.html", context)


class WithdrawalBtcWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'withdrawal_money/withdraw.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = WithdrawalRequest(payment_system='BTC',
                                   amount=form_data[0]['amount'],
                                   address=form_data[1]['address'],
                                   name=form_data[1]['name'],
                                   user=self.request.user)
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        context = super(WithdrawalBtcWizard, self).get_context_data(**kwargs) | {
            'system': 'BTC wallet address',
            'name': 'Bitcoin'
        }
        return context


# @login_required
# def withdrawal_usdt(request):

#     form = WithdrawalUsdtForm(request.POST or None)
#     if form.is_valid():
#         ticket = form.save(commit=False)
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'USDT wallet address',
#         'name': 'USDT'
#     }
#     return render(request, "withdrawal_money/withdraw.html", context)


class WithdrawalUsdtWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'withdrawal_money/withdraw.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = WithdrawalRequest(payment_system='USDT',
                                   amount=form_data[0]['amount'],
                                   address=form_data[1]['address'],
                                   name=form_data[1]['name'],
                                   user=self.request.user)
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        context = super(WithdrawalUsdtWizard, self).get_context_data(**kwargs) | {
            'system': 'USDT wallet address',
            'name': 'USDT'
        }
        return context


# @login_required
# def withdrawal_eth(request):

#     form = WithdrawalEthForm(request.POST or None)
#     if form.is_valid():
#         ticket = form.save(commit=False)
#         ticket.user = request.user
#         ticket.save()
#         return redirect('/')

#     context = {
#         'form': form,
#         'system': 'ETH wallet address',
#         'name': 'Ethereum'
#     }
#     return render(request, "withdrawal_money/withdraw.html", context)


class WithdrawalEthWizard(SessionWizardView):
    form_list = FORMS
    template_name = 'withdrawal_money/withdraw.html'

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        ticket = WithdrawalRequest(payment_system='ETH',
                                   amount=form_data[0]['amount'],
                                   address=form_data[1]['address'],
                                   name=form_data[1]['name'],
                                   user=self.request.user)
        ticket.save()
        return redirect('/')

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_context_data(self, **kwargs):
        context = super(WithdrawalEthWizard, self).get_context_data(**kwargs) | {
            'system': 'ETH wallet address',
            'name': 'Ethereum'
        }
        return context
