from django.contrib import admin
from subscriptions.models import SubscribeModel


class SubscribeModelAdmin(admin.ModelAdmin):
    model = SubscribeModel
    list_display = ('email', 'status', 'created_date', 'updated_date')
    list_filter = ['status', 'created_date']
    search_fields = ['status', 'created_date']


admin.site.register(SubscribeModel, SubscribeModelAdmin)
