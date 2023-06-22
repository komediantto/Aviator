from django import forms
from .models import WithdrawalRequest
import logging

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = WithdrawalRequest

        fields = [
            "amount",
        ]


class WithdrawalForm2(forms.ModelForm):
    class Meta:
        model = WithdrawalRequest

        fields = [
            "address",
            "name"
            ]

    def clean(self):
        cleaned_data = super().clean()
        address = cleaned_data.get('address')
        name = cleaned_data.get('name')
        if not address:
            raise forms.ValidationError("This field couldn't be empty")
        if not name:
            raise forms.ValidationError("This field couldn't be empty")
        return cleaned_data


# class WithdrawalUpiForm(forms.ModelForm):
#     class Meta:
#         model = WithdrawalUpi

#         fields = [
#             "address",
#             "name",
#             "amount",
#         ]


# class WithdrawalPhonePeForm(forms.ModelForm):
#     class Meta:
#         model = WithdrawalPhonePe

#         fields = [
#             "address",
#             "name",
#             "amount",
#         ]


# class WithdrawalBtcForm(forms.ModelForm):
#     class Meta:
#         model = WithdrawalBtc

#         fields = [
#             "address",
#             "name",
#             "amount",
#         ]


# class WithdrawalUsdtForm(forms.ModelForm):
#     class Meta:
#         model = WithdrawalUsdt

#         fields = [
#             "address",
#             "name",
#             "amount",
#         ]


# class WithdrawalEthForm(forms.ModelForm):
#     class Meta:
#         model = WithdrawalEth

#         fields = [
#             "address",
#             "name",
#             "amount",
#         ]
