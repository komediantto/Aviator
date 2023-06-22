from django.contrib import admin


from .models import WithdrawalRequest


class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'address', 'name')
    search_fields = ('user',)



admin.site.register(WithdrawalRequest, WithdrawalAdmin)
