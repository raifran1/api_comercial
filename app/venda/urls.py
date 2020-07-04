from django.urls import path
from .views import VendaList, VendaMethodObject, VendasProdList, VendasProdMethodObject

urlpatterns = [
    path('vendas/', VendaList.as_view()),
    path('venda/<int:pk>/', VendaMethodObject.as_view()),
    path('produtos-vendas/', VendasProdList.as_view()),
    path('produtos-venda/<int:id>/', VendasProdMethodObject.as_view()),
]