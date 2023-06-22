from django.db import models
from urls_for_ticket.models import TempAcc

from django.contrib.auth.models import User
from .validators import card_validator


class PaymentRequest(models.Model):

    class Meta:
        verbose_name = 'Заявка на пополнение'
        verbose_name_plural = 'Заявки на пополнение'

    amount = models.FloatField()
    payment_system = models.TextField(max_length=20, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    href = models.ForeignKey(TempAcc, on_delete=models.CASCADE,
                             null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)


class Google(models.Model):

    class Meta:
        verbose_name = 'Реквизиты Google'
        verbose_name_plural = 'Реквизиты Google'

    number_of_card = models.CharField(max_length=16,
                                      validators=[card_validator, ])
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.number_of_card}\n{self.name}'


class Upi(models.Model):

    class Meta:
        verbose_name = 'Реквизиты Upi'
        verbose_name_plural = 'Реквизиты Upi'

    upi_id = models.IntegerField()

    def __str__(self):
        return str(self.upi_id)


class PhonePe(models.Model):

    class Meta:
        verbose_name = 'Реквизиты PhonePe'
        verbose_name_plural = 'Реквизиты PhonePe'

    phone_number = models.CharField(max_length=12, default='')

    def __str__(self):
        return self.phone_number


class Btc(models.Model):

    class Meta:
        verbose_name = 'Биткоин кошелёк'
        verbose_name_plural = 'Биткоин кошельки'

    address_of_btc = models.CharField(max_length=100)

    def __str__(self):
        return self.address_of_btc


class Usdt(models.Model):

    class Meta:
        verbose_name = 'USDT кошелёк'
        verbose_name_plural = 'USDT кошельки'

    address_of_usdt = models.CharField(max_length=100)

    def __str__(self):
        return self.address_of_usdt


class Eth(models.Model):

    class Meta:
        verbose_name = 'Etherium кошелёк'
        verbose_name_plural = 'Etherium кошельки'

    address_of_eth = models.CharField(max_length=100)

    def __str__(self):
        return self.address_of_eth
