from django import forms
from .models import Cuenta, Transaccion

class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = ['tipo_cuenta']

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['cuenta_destino', 'monto', 'descripcion']
