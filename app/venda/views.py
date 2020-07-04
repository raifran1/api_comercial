from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Venda, VendasProd
from .serializers import VendaSerializer, VendasProdSerializer

class VendaList(APIView):
    """
    Methods HTTP - GET ALL, POST OBJECT
    """
    def get(self, request, format=None):
        venda = Venda.objects.all()
        serializer = VendaSerializer(venda, many=True)
        return Response(serializer.data)

    # post object
    def post(self, request, format=None):
        serializer = VendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendaMethodObject(APIView):
    """
    Methods HTTP - GET OBJECT DETAIL, PUTH, DELETE
    """
    # get object
    def get_object(self, pk):
        try:
            return Venda.objects.get(pk=pk)
        except Venda.DoesNotExist:
            raise Http404

    # get object or all
    def get(self, request, pk, format=None):
        venda = self.get_object(pk)
        serializer = VendaSerializer(venda)
        return Response(serializer.data)

    # put object
    def put(self, request, pk, format=None):
        venda = self.get_object(pk)
        serializer = VendaSerializer(venda, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        venda = self.get_object(pk)
        venda.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VendasProdList(APIView):
    """
    Methods HTTP - GET ALL, POST OBJECT
    """
    def get(self, request, format=None):
        vendasprod = VendasProd.objects.all()
        serializer = VendasProdSerializer(vendasprod, many=True)
        return Response(serializer.data)

    # post object
    def post(self, request, format=None):
        serializer = VendasProdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendasProdMethodObject(APIView):
    """
    Methods HTTP - GET OBJECT DETAIL, PUTH, DELETE
    """
    # get object
    def get_object(self, pk):
        try:
            return VendasProd.objects.get(pk=pk)
        except VendasProd.DoesNotExist:
            raise Http404

    # get object or all
    def get(self, request, pk, format=None):
        vendasprod = self.get_object(pk)
        serializer = VendasProdSerializer(vendasprod)
        return Response(serializer.data)

    # put object
    def put(self, request, pk, format=None):
        vendasprod = self.get_object(pk)
        serializer = VendasProdSerializer(vendasprod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vendasprod = self.get_object(pk)
        vendasprod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)