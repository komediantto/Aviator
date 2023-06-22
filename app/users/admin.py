from django.contrib import admin
from .models import CustomUser
from django.utils.html import format_html


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'room_link')
    search_fields = ('user',)

    def room_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.room.url)

    def username(self, obj):
        return obj.user.username

    def password(self, obj):
        return obj.user.password


admin.site.register(CustomUser, UserAdmin)
