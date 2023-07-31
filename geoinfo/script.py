#!/usr/bin/env python
import os


def main():
    """
    Run alternative start script.
    """

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoinfo.settings')

    from django.core.wsgi import get_wsgi_application
    get_wsgi_application()

    from django.core.management import call_command
    call_command('runserver',  '127.0.0.1:8000')


if __name__ == '__main__':
    main()
