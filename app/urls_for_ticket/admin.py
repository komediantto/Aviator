from django.contrib import admin
from .models import TempAcc
from django.utils.html import format_html

class TempAccAdmin(admin.ModelAdmin):
    list_display = ('tempacc_link', 'date_added')
    search_fields = ('date_added',)

    def tempacc_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)


admin.site.register(TempAcc, TempAccAdmin)
