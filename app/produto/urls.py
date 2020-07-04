from django.urls import path
from .views import ProdutoList, ProdutoMethodObject, CategoriaList, CategoriaMethodObject

urlpatterns = [
    path('produtos/', ProdutoList.as_view()),
    path('produto/<int:pk>/', ProdutoMethodObject.as_view()),
    path('categorias/', CategoriaList.as_view()),
    path('categoria/<int:id>/', CategoriaMethodObject.as_view()),
]