from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cuenta, Transaccion, Cliente
from .forms import CuentaForm, TransaccionForm

@login_required
def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaForm(request.POST)
        if form.is_valid():
            cuenta = form.save(commit=False)
            cuenta.cliente = Cliente.objects.get(user=request.user)
            cuenta.numero_cuenta = 'CU' + str(Cuenta.objects.count() + 1000)
            cuenta.saldo = 100.00  # 💰 Monto inicial
            cuenta.save()
            return redirect('dashboard')
    else:
        form = CuentaForm()
    return render(request, 'usuarios/crear_cuenta.html', {'form': form})

@login_required
def dashboard(request):
    try:
        cliente = Cliente.objects.get(user=request.user)
    except Cliente.DoesNotExist:
        # Si no existe el cliente, redirigimos para crear cuenta
        return redirect('crear_cuenta')

    cuentas = Cuenta.objects.filter(cliente=cliente)
    return render(request, 'usuarios/dashboard.html', {'cuentas': cuentas})

@login_required
def transferencia(request, cuenta_id):
    cuenta_origen = get_object_or_404(Cuenta, id=cuenta_id)
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            transaccion = form.save(commit=False)
            if cuenta_origen.saldo >= transaccion.monto:
                cuenta_destino = transaccion.cuenta_destino
                cuenta_origen.saldo -= transaccion.monto
                cuenta_destino.saldo += transaccion.monto
                cuenta_origen.save()
                cuenta_destino.save()
                transaccion.cuenta_origen = cuenta_origen
                transaccion.save()
                return redirect('dashboard')
            else:
                form.add_error('monto', 'Saldo insuficiente.')
    else:
        form = TransaccionForm()
    return render(request, 'usuarios/transferencia.html', {'form': form, 'cuenta': cuenta_origen})
