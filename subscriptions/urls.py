from django.urls import path
from subscriptions.views import SubscribeView, subscription_confirmation

app_name = 'subscriptions'

urlpatterns = [
    path('', SubscribeView, name='subscribe'),
    path('confirm/', subscription_confirmation,
         name='subscription_confirmation')
]
