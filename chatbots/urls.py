from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('chatbots/', views.chatbots, name='chatbots'),
    path('chat_bot', views.chat_bot, name='chat_bot'),
    path('motor_bot', views.motor_bot, name='motor_bot'),
    path('health_bot', views.health_bot, name='health_bot'),
]