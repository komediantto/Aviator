from django import forms
from .models import Google, Upi, PhonePe, PaymentRequest, Btc, Usdt, Eth


class GoogleForm(forms.ModelForm):
    class Meta:
        model = Google

        fields = [
            "number_of_card",
            "name"
        ]


class UpiForm(forms.ModelForm):
    class Meta:
        model = Upi

        fields = [
            "upi_id",
        ]


class PhonePeForm(forms.ModelForm):
    class Meta:
        model = PhonePe

        fields = [
            "phone_number",
        ]


class PaymentRequestForm1(forms.ModelForm):
    class Meta:
        model = PaymentRequest

        fields = [
            "amount",
        ]

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount is not None and (amount < 10000 or amount > 50000):
            raise forms.ValidationError(
                "Amount must be between 10000 and 50000.")
        return amount


class PaymentRequestForm2(forms.ModelForm):
    class Meta:
        model = PaymentRequest

        fields = [
            "transaction_id",
        ]


class BtcForm(forms.ModelForm):
    class Meta:
        model = Btc

        fields = [
            "address_of_btc",
        ]


class UsdtForm(forms.ModelForm):
    class Meta:
        model = Usdt

        fields = [
            "address_of_usdt",
        ]


class EthForm(forms.ModelForm):
    class Meta:
        model = Eth

        fields = [
            "address_of_eth",
        ]
