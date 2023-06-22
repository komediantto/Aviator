from django.core.validators import RegexValidator


card_validator = RegexValidator(
    regex=r'\d{16}',
    message='Введите 16 цифр номера карты без пробелов')
