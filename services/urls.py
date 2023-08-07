from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('bot_listing', views.bot_listing, name='bot_listing'),
    path('ml', views.ml, name='ml'),
    path('custom_apps', views.custom_apps, name='custom_apps'),
    path('auto_cloud', views.auto_cloud, name='auto_cloud'),
    path('commerce', views.commerce, name='auto_cloud'),
    path('market_automation', views.market_automation, name='market_automation')
]