from django.urls import path
from .views import ClienteList, ClienteMethodObject, EnderecoList, EnderecoMethodObject

urlpatterns = [
    path('clientes/', ClienteList.as_view()),
    path('cliente/<int:pk>/', ClienteMethodObject.as_view()),

    path('enderecos/', EnderecoList.as_view()),
    path('endereco/<int:id>', EnderecoMethodObject.as_view()),
]