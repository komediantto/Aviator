from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from . import validators


class WithdrawalRequest(models.Model):

    class Meta:
        verbose_name = 'Заявка на вывод'
        verbose_name_plural = 'Заявки на вывод'

    payment_system = models.TextField(max_length=20, default=None)
    address = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    amount = models.FloatField(validators=[validators.validate_amount,])
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)




# class WithdrawalUpi(models.Model):

#     class Meta:
#         verbose_name = 'Upi'
#         verbose_name_plural = 'Upi'

#     address = models.IntegerField()
#     amount = models.FloatField(validators=[validators.validate_amount,])
#     name = models.CharField(max_length=100, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              null=True, blank=True)


# class WithdrawalBtc(models.Model):

#     class Meta:
#         verbose_name = 'Биткоин'
#         verbose_name_plural = 'Биткоины'

#     address = models.CharField(max_length=100)
#     amount = models.FloatField(validators=[validators.btc_validate])
#     name = models.CharField(max_length=100, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              null=True, blank=True)


# class WithdrawalUsdt(models.Model):

#     class Meta:
#         verbose_name = 'USDT'
#         verbose_name_plural = 'USDT'

#     address = models.CharField(max_length=100)
#     amount = models.FloatField(validators=[validators.usdt_validate])
#     name = models.CharField(max_length=100, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              null=True, blank=True)


# class WithdrawalEth(models.Model):

#     class Meta:
#         verbose_name = 'Эфир'
#         verbose_name_plural = 'Эфир'

#     address = models.CharField(max_length=100)
#     amount = models.FloatField(validators=[validators.eth_validate])
#     name = models.CharField(max_length=100, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              null=True, blank=True)


# class WithdrawalPhonePe(models.Model):

#     class Meta:
#         verbose_name = 'PhonePe'
#         verbose_name_plural = 'PhonePe'

#     address = models.CharField(max_length=12)
#     amount = models.FloatField(validators=[validators.validate_amount,])
#     name = models.CharField(max_length=100, null=True, blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE,
#                              null=True, blank=True)
