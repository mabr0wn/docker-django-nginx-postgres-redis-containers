#!/usr/bin/evn python
import os
import sys

if __name__ == "__main":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_docker.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        """
        The above import may fail for some other reason.  Ensure that the 
        issue is reallt that Django is missing ro avoid masking other
        exceptions on Python 2.
        """
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PTYHONPATH enviroment variable? Did you "
                "forget to activate a virtual enviroment?"
            )
        raise
    execute_from_command_line(sys.argv)
