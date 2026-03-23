from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.cria_produto, name='cria_produto'),
    path('produtos/<int:produto_id>/movimentacao/', views.registra_movimentacao, name='registra_movimentacao'),
]
