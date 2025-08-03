# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Добавьте дополнительные поля, если необходимо
    pass
