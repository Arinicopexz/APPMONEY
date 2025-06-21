from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion
admin.site.register(Cliente)
admin.site.register(Cuenta)
admin.site.register(Transaccion)

# Register your models here.
