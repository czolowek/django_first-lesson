```python
import os
import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.db import models
from django.http import HttpResponse
from django.urls import path

# --- Налаштування Django ---
BASE_DIR = os.path.dirname(__file__)
settings.configure(
    DEBUG=True,
    SECRET_KEY="secret",
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    },
    INSTALLED_APPS=[
        "django.contrib.contenttypes",
        "django.contrib.auth",
        "mainapp",  # наша апка
    ],
)

# --- Модель ---
class Person(models.Model):
    first_name = models.CharField(max_length=30)     # ім’я
    last_name = models.CharField(max_length=30)      # прізвище
    birth_date = models.DateField()                  # дата народження
    age = models.IntegerField()                      # вік
    email = models.CharField(max_length=100)         # пошта

    class Meta:
        app_label = "mainapp"

# --- View ---
def home(request):
    return HttpResponse("Django працює! Спробуй додати/подивитись базу через ORM.")

urlpatterns = [
    path("", home),
]

# --- Запуск ---
if __name__ == "__main__":
    execute_from_command_line(sys.argv)
```
