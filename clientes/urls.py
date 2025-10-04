from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('novo/', views.criar_cliente, name='criar_cliente'),
    path('editar/<int:id>', views.atualizar_cliente, name='atualizar_cliente'),
    path('remover_cliente/<int:id>', views.remover_cliente, name='remover_cliente'),
]