from django.urls import path
from .views import ClienteList, ClienteMethodObject, EnderecoList, EnderecoMethodObject

urlpatterns = [
    path('', ClienteList.as_view()),
    path('<int:pk>/', ClienteMethodObject.as_view()),

    path('enderecos/', EnderecoList.as_view()),
    path('enderecos/<int:id>', EnderecoMethodObject.as_view()),
]