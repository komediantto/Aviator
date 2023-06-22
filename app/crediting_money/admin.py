from django.contrib import admin

from .models import Google, Upi, PhonePe, PaymentRequest, Btc, Eth, Usdt


class GoogleAdmin(admin.ModelAdmin):
    list_display = ('number_of_card', 'name')
    search_fields = ('name',)


class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'href', 'amount', 'payment_system')
    search_fields = ('payment_system',)


class UpiAdmin(admin.ModelAdmin):
    list_display = ('upi_id',)
    search_fields = ('upi_id',)


class EthAdmin(admin.ModelAdmin):
    list_display = ('address_of_eth',)
    search_fields = ('address_of_eth',)


class UsdtAdmin(admin.ModelAdmin):
    list_display = ('address_of_usdt',)
    search_fields = ('address_of_usdt',)


class BtcAdmin(admin.ModelAdmin):
    list_display = ('address_of_btc',)
    search_fields = ('address_of_btc',)


class PhonePeAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    search_fields = ('phone_numbers',)


admin.site.register(PaymentRequest, PaymentRequestAdmin)
admin.site.register(Google, GoogleAdmin)
admin.site.register(Upi, UpiAdmin)
admin.site.register(PhonePe, PhonePeAdmin)
admin.site.register(Btc, BtcAdmin)
admin.site.register(Eth, EthAdmin)
admin.site.register(Usdt, UsdtAdmin)
