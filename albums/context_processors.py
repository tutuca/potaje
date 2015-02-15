import random
import os
from glob import glob
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.templatetags.staticfiles import static


def random_background(request):
    '''
    Choose a webm file from static_root and return the url by susbtitution.
    Adds the `background` dict with `url` and `poster` like this:

    background = {
        'url': '/static/bg/background.webm',
        'poster': '/static/bg/background_poster.png'
    }

    '''
    files = glob('%s/*.gif' % finders.find('bg/'))
    bg_choice = os.path.basename(random.choice(files))

    bg_url = static(bg_choice)
    return {
        'background_url': bg_url,
    }
