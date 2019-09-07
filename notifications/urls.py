from django.urls import path
from notifications.views import (
    NotificationListView,
    ShowNotificationView,
    DeleteNotificationView
)
app_name = 'notifications'

urlpatterns = [
    path('', NotificationListView, name='notifications'),
    path('show/<notification_id>/', ShowNotificationView, name='show_notification'),
    path('delete/<notification_id>/',
         DeleteNotificationView, name='delete_notification'),
]
