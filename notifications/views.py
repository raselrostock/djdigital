from django.shortcuts import render, redirect
from notifications.models import Notification


# Show the list of all notifications
def NotificationListView(request):
    notifications = Notification.objects.filter(
        user=request.user).all().order_by('-notification_at')
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})


# Show a specific notification
def ShowNotificationView(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.viewed = True
    notification.save()
    return render(request, 'notifications/notifications_show.html', {'notification': notification})


# Delete a specific notification
def DeleteNotificationView(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.delete()
    return redirect('notifications:notifications')
