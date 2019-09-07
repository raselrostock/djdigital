from django.shortcuts import redirect
import logging
import traceback
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from subscriptions.encdecutility.enc_dec_util import *
SUBSCRIBE_STATUS = 'subscribed'
SEPARATOR = '&'


def subscription_confirmation(request):
    if request.method == 'POST':
        raise Http404

    token = request.GET.get('token', None)
    if not token:
        logging.getLogger('error_logger').warning('Invalid Link')
        messages.error(request, "Invalid Link")
        return redirect('memberships:dashboard')

    token = decrypt(token)
    if token:
        token = token.split(SEPARATOR)
        email = token[0]
        initiate_time = token[1]
        try:
            subscribe_model_instance = SubscribeModel.objects.get(email=email)
            subscribe_model_instance.status = SUBSCRIBE_STATUS
            subscribe_model_instance.updated_date = timezone.now()
            subscribe_model_instance.save()
            messages.success(request, 'Subscription Confirmed. Thank you.')
        except ObjectDoesNotExist as e:
            logging.getLogger('error_logger').warning(traceback.format_exc())
            messages.error(request, 'Invalid Link')
    else:
        logging.getLogger('error_logger').warning('Invalid token')
        messages.error(request, 'Invalid Link')
    return redirect('memberships:dashboard')
