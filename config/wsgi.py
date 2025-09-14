"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os


# Установите переменную окружения для SECRET_KEY (не рекомендуется для продакшн)
os.environ['SECRET_KEY'] = 'NQBghmmXmpGd-6gzhWD20PmAeZGSjdjOscBHkkBwptd5NFR9Wi97KHKLKRZrR78aTjE'

# Убедитесь, что переменная окружения DJANGO_SETTINGS_MODULE установлена
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Импортируйте get_wsgi_application после установки переменной окружения
from django.core.wsgi import get_wsgi_application

# Получите WSGI-приложение
application = get_wsgi_application()

# Если нужно, вы можете вывести SECRET_KEY для отладки (не рекомендуется в продакшн)
print(os.environ['SECRET_KEY'])

