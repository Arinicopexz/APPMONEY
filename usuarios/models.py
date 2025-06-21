from django.db import models
from django.contrib.auth.models import User

# Cliente con relación uno a uno al usuario del sistema
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cedula = models.CharField(max_length=10, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

# Cuenta bancaria
class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=20, unique=True)
    tipo_cuenta = models.CharField(max_length=20, choices=[('ahorro', 'Ahorro'), ('corriente', 'Corriente')])
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_cuenta} - {self.cliente}"

# Transacciones
class Transaccion(models.Model):
    cuenta_origen = models.ForeignKey(Cuenta, related_name='transacciones_enviadas', on_delete=models.CASCADE)
    cuenta_destino = models.ForeignKey(Cuenta, related_name='transacciones_recibidas', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cuenta_origen} → {self.cuenta_destino} (${self.monto})"
