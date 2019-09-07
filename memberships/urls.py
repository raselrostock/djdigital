from django.urls import path
from memberships.views import (
    DashboardView,
    MembershipListView,
    PaymentView,
    updateTransactionRecords,
    CancelSubscription
)

app_name = 'memberships'
urlpatterns = [
    path('', DashboardView, name='dashboard'),
    path('select/', MembershipListView.as_view(), name='select'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('update-transactions/<subscription_id>/',
         updateTransactionRecords, name='update-transactions'),
    path('cancel/', CancelSubscription, name='cancel')
]
