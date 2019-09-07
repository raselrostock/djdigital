
from .utility_functionality import *
from django.contrib import messages
from django.shortcuts import redirect, reverse


def updateTransactionRecords(request, subscription_id):
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)
    user_membership.membership = selected_membership
    user_membership.save()
    sub, created = Subscription.objects.get_or_create(
        profile=user_membership)
    sub.stripe_subscription_id = subscription_id
    sub.active = True
    sub.save()
    try:
        del request.session['selected_membership_type']
    except:
        pass
    messages.success(request, f'Successfull { selected_membership } created')
    return redirect(reverse('memberships:select'))
