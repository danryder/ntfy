from sys import platform
from importlib import import_module


def notify(title, message, **kwargs):
    for os in ['linux', 'win32', 'darwin']:
        if platform.startswith(os):
            module = import_module('ntfy.backends.{}'.format(os))
            module.notify(title=title, message=message, **kwargs)
            break
