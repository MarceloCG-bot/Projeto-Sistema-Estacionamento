from django.urls import path
from django.urls.conf import include
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movrotativos,
    lista_mensalista,
    lista_movmensalista,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrotativos_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativos_delete,
    mensalista_delete,
    movmensalista_delete
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<id>/', pessoa_delete, name='core_pessoa_delete'),
    
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculo-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<id>/', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<id>/', veiculo_delete, name='core_veiculo_delete'),
    
    path('mov-rot/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rot-novo/', movrotativos_novo, name='core_movrotativos_novo'),
    path('mov-rot-update/<id>/', movrotativos_update, name='core_movrotativos_update'),
    path('mov-rot-delete/<id>/', movrotativos_delete, name='core_movrotativos_delete'),
    
    path('mensalistas/', lista_mensalista, name='core_lista_mensalista'),
    path('mensalista-novo/', mensalista_novo, name='core_mensalista_novo'),
    path('mensalista-update/<id>/', mensalista_update, name='core_mensalista_update'),
    path('mensalista-delete/<id>/', mensalista_delete, name='core_mensalista_delete'),
    
    path('mov-mensal/', lista_movmensalista, name='core_lista_movmensalista'),
    path('mov-mensal-novo/', movmensalista_novo, name='core_movmensalista_novo'),
    path('mov-mensal-update/<id>/', movmensalista_update, name='core_movmensalista_update'),
    path('mov-mensal-delete/<id>/', movmensalista_delete, name='core_movmensalista_delete'),
]