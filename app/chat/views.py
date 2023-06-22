from django.shortcuts import render, redirect
from .models import Message, Room
from django.contrib.auth.decorators import login_required
import logging


@login_required
def index(request):
    return render(request, 'chat/index.html')


@login_required
def room(request, room_name):
    username = request.GET.get('username', 'Поддержка')
    chat_user = room_name.split('_')[0]
    logging.info(chat_user)
    logging.info(request.user.username)
    if request.user.username != chat_user and not request.user.is_staff:
        return redirect('/')
    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=room.pk)[0:25]
    return render(request, 'chat/room.html', {'room_name': room_name,
                                              'username': username,
                                              'messages': messages})
