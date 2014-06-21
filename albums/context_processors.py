import random
import os
from glob import glob
from django.contrib import staticfiles
from django.conf import settings


def random_background(request):
    '''
    Choose a webm file from static_root and return the url by susbtitution.
    Adds the `background` dict with `url` and `poster` like this:

    background = {
        'url': '/static/bg/background.webm',
        'poster': '/static/bg/background_poster.png'
    }

    '''
    files = glob('%s/*.webm' % staticfiles.finders.find('bg/'))
    bg_choice = os.path.basename(random.choice(files))
    bg_url = settings.STATIC_URL + 'bg/' + bg_choice

    poster = bg_url.replace('.webm', '_poster.png')

    return {
        'background': {
            'url': bg_url,
            'poster': poster
        }
    }
