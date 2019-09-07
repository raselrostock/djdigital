from django.shortcuts import render, redirect, reverse
from time import time
import datetime
import logging
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from subscriptions.validation_utility import validate_email
from subscriptions.models import SubscribeModel
from django.utils import timezone
from subscriptions.encdecutility.enc_dec_util import *
from subscriptions.email_utility import *
SUBSCRIBE_STATUS = 'subscribed'
SEPARATOR = '&'


def save_email(email):
    try:
        subscribe_model_instance = SubscribeModel.objects.get(email=email)
    except ObjectDoesNotExist as e:
        subscribe_model_instance = SubscribeModel()
        subscribe_model_instance.email = email
        subscribe_model_instance.created_date = timezone.now()
    except Exception as e:
        return False

    subscribe_model_instance.status = SUBSCRIBE_STATUS
    subscribe_model_instance.updated_date = timezone.now()
    subscribe_model_instance.save()
    return True


def SubscribeView(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        email = post_data.get('email', None)
        error_msg = validate_email(email)
        if error_msg:
            messages.error(request, error_msg)
            return redirect('home')

        save_status = save_email(email)
        if save_status:
            token = encrypt(email + SEPARATOR + str(datetime.time()))
            subscription_confirmation_url = request.build_absolute_uri(
                reverse('subscriptions:subscription_confirmation'))+'?token='+token
            status = send_subscription_email(
                email, subscription_confirmation_url)
            if not status:
                SubscribeModel.objects.get(email=email).delete()
                logging.getLogger('info_logger').info('Deleted the record from Subscribe table for '+email +
                                                      " as email sending failed. status: " + str(status))
            else:
                msg = "Mail sent to email Id '" + email + "'. Please confirm your subscription by clicking on " \
                    "confirmation link provided in email. " \
                    "Please check your spam folder as well."
                logging.getLogger("error_logger").error("Hi I am here")
                messages.success(request, msg)

        else:
            msg = "Some error occurred. Please try in some time. Meanwhile we are looking into it."
            messages.error(request, msg)
        return redirect('memberships:dashboard')
