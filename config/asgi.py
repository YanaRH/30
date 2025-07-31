"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

# Установите SECRET_KEY вручную (не рекомендуется для продакшн)
os.environ['SECRET_KEY'] = 'NQBghmmXmpGd-6gzhWD20PmAeZGSjdjOscBHkkBwptd5NFR9Wi97KHKLKRZrR78aTjE'

SECRET_KEY = os.getenv('SECRET_KEY')
print(SECRET_KEY)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Убрали вызов get_asgi_application()
# application = get_asgi_application()

