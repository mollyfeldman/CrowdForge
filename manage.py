#!/usr/bin/env python
#Followed instructions here to set up virtual environment: https://djangowaves.com/tips-tricks/fix-import-error-no-module-named-django-core-management/
#Currently get this error:
#ImportError: Could not import settings 'CrowdForge.settings' (Is it on sys.path? Does it have syntax errors?): No module named settings
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
