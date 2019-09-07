from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
import logging


def HomeView(request):
    # Translation
    # from django.utils import translation
    # user_language = 'de'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del resquest.session[translation.LANGUAGE_SESSION_KEY]
    ##############################
    title = _('Home')
    context = {
        'title': title
    }
    return render(request, 'home.html', context)


def bad_request(request, exception=None, template_name='400.html'):
    return render(request, 'errors/400.html')


def permission_denied(request, exception=None, template_name='403.html'):
    return render(request, 'errors/403.html')


def not_found(request, exception=None, template_name='404.html'):
    return render(request, 'errors/404.html')


def server_error(request, exception=None, template_name='500.html'):
    return render(request, 'errors/500.html')
