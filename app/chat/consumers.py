import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from transliterate import translit
from users.models import User

from .models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        english_name = translit(self.room_name,
                                language_code='ru', reversed=True)
        correct_english_name = english_name.replace(' ', '_').replace("'", '')
        self.room_group_name = 'chat_%s' % correct_english_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = await Room.objects.aget(name=data['room'])

        await self.save_message(username, room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room': room.name,
                'room_url': room.url
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        room_url = event['room_url'].split('?')

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username
        }))
        await self.send_email(username, room, room_url[0], message)

    @sync_to_async
    def save_message(self, username, room, message):
        Message.objects.create(username=username, room=room, content=message)

    @sync_to_async
    def send_email(self, username, room, room_url, message):
        admins = User.objects.filter(is_staff=True)
        current_site = str(Site.objects.get_current()) + room_url
        emails = []
        for admin in admins:
            emails.append(admin.email)
        email = EmailMessage(
            subject='Новое сообщение',
            body=(f'Пользователь {username} обратился в поддержку.\n\n'
                  f'Текст сообщения: {message}\n\n'
                  f'Ссылка на чат: http://{current_site}'),
            to=emails,
        )
        if username != 'Поддержка':
            email.send()
