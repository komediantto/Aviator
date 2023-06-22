from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from .const import ERROR
import requests
import logging


card_validator = RegexValidator(
    regex=r'\d{16}',
    message='Введите 16 цифр номера карты без пробелов')


def validate_amount(value):
    if value < 10000 or value > 50000:
        raise ValidationError(ERROR)


def validate_address(value):
    if not value:
        raise ValidationError('Это поле не можеть быть пустым')


def btc_validate(value):
    response = requests.get('https://blockchain.info/ticker')
    exchange = response.json()['RUB']['last']
    rub = float(value)*float(exchange)
    if rub < 10000 or rub > 50000:
        raise ValidationError(ERROR)


def eth_validate(value):
    response = requests.get(
        'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=RUB')
    exchange = response.json()['RUB']
    rub = float(value)*float(exchange)
    if rub < 10000 or rub > 50000:
        raise ValidationError(ERROR)


def usdt_validate(value):
    response = requests.get(
        'https://min-api.cryptocompare.com/data/price?fsym=USDT&tsyms=RUB')
    exchange = response.json()['RUB']
    rub = float(value)*float(exchange)
    if rub < 10000 or rub > 50000:
        raise ValidationError(ERROR)
