from .utility_functionality import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from decouple import config
import stripe


def CancelSubscription(request):
    user_subscription = get_user_subscription(request)
    if user_subscription.active is False:
        messages.error(request, 'You donot have active subscription')
        logging.getLogger("error_logger").error(
            "You donot have active subscription")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    sub = stripe.Subscription.retrieve(
        user_subscription.stripe_subscription_id)
    del sub

    user_subscription.active = False
    user_subscription.save()

    user_membership = get_user_membership(request)
    free_membership = Membership.objects.get(membership_type='Free')
    user_membership.membership = free_membership
    user_membership.save()

    messages.success(request, 'Successfully cancel the subscription')
    return redirect(reverse('memberships:select'))
