import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'leya.settings.settings'

# ===========
# Add any python 3rd party module that doesnt exist at
# https://developers.google.com/appengine/docs/python/tools/libraries27
# ===========
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'leya/libs'))
# ===========

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch

# Log errors.
#import logging
#def log_exception(*args, **kwds):
#    logging.exception('Exception in request:')
#
#django.dispatch.Signal.connect(
#    django.core.signals.got_request_exception, log_exception)

# Unregister the rollback event handler.
django.dispatch.Signal.disconnect(
    django.core.signals.got_request_exception,
    django.db._rollback_on_exception)

app = django.core.handlers.wsgi.WSGIHandler()
