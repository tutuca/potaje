import random
import os
from glob import glob
from django.contrib.staticfiles import finders

from django.conf import settings
from . import models


def random_background(request):
    """
    Choose a webm file from static_root and return the url by susbtitution.
    Adds the `background` dict with `url` and `poster` like this:

    background = {
        'url': '/static/bg/background.webm',
        'poster': '/static/bg/background_poster.png'
    }

    """
    bg_url = ""

    files = glob("%s/*.gif" % finders.find("bg/"))

    if files:
        bg_choice = os.path.basename(random.choice(files))
        bg_url = settings.STATIC_URL + "bg/" + bg_choice

    return {
        "background": bg_url,
    }


def sections(request):
    sections = models.Section.objects.select_related().all()
    return {"sections": sections}
