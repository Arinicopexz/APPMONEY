from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path('transferencia/<int:cuenta_id>/', views.transferencia, name='transferencia'),
]
