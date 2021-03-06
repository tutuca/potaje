#!/usr/bin/env python
import os
import sys


def do_manage():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "potaje.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    do_manage()
