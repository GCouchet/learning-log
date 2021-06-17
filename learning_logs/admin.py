from django.contrib import admin
from learning_logs.models import Topic, Entry # el punto hace que busce models en la misma carpeta que admin

# Register your models here.

admin.site.register(Topic)  # hace que el admin pueda manejar los modelos desde el sitio de adeministrador
admin.site.register(Entry)