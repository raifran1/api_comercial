from django.urls import path
from .views import SetorList, SetorMethodObject, FuncionarioList, FuncionarioMethodObject

urlpatterns = [
    path('setores/', SetorList.as_view()),
    path('setor/<int:pk>/', SetorMethodObject.as_view()),
    path('funcionarios/', FuncionarioList.as_view()),
    path('funcionario/<int:id>', FuncionarioMethodObject.as_view()),
]