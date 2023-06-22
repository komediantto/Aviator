"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('chat/', include('chat.urls')),
    path('withdrawal/', include(('withdrawal_money.urls',
                                 'withdrawal_money'),
                                namespace="withdrawal_money")),
    path('', include(('crediting_money.urls', 'crediting_money'),
                     namespace='crediting_money')),
    path('tempacc/', include(
        ('urls_for_ticket.urls', 'urls_for_ticket'),
        namespace='urls_for_ticket'))
]
