from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from django.dispatch import receiver
from courses.models import Course
from django.conf import settings


class Notification(models.Model):
    title = models.CharField(max_length=256)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    notification_at = models.DateTimeField(
        verbose_name="Notification Create At", auto_now_add=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_read_url(self):
        return reverse("notifications:seen_notification", kwargs={"notification_id": self.id})

    def get_notification_url(self):
        return reverse("notifications:show_notification", kwargs={"notification_id": self.id})


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_coursenotification_message(sender, *args, **kwargs):
    if kwargs.get('created', False):
        Notification.objects.create(user=kwargs.get('instance'),
                                    title='Welcome to Rostocker Labs Digital Services',
                                    message='Thank you for signing up')
