from django.contrib import admin
from django.utils.html import format_html
from .models import Message, Room


class MessageAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'room')
    search_fields = ('username',)
    list_filter = ('username',)


class MessageInline(admin.StackedInline):
    model = Message
    extra = 0


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_link', 'date_added')
    search_fields = ('name',)
    list_filter = ('date_added',)
    inlines = [
        MessageInline,
    ]

    def room_link(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)


admin.site.register(Message, MessageAdmin)
admin.site.register(Room, RoomAdmin)
