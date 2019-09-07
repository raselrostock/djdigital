import os
from .base import *
""" ----------------------------------------
    Translation
    ----------------------------------------
"""
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('EN')),
    ('de', _('DE')),
)
LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'de'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
# Static files (CSS, JavaScript, Images)
