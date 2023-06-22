from django.apps import AppConfig


class WithdrawalMoneyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'withdrawal_money'
    verbose_name = 'Заявки на вывод'
