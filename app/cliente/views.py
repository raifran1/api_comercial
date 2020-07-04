from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cliente, Endereco
from .serializers import ClienteSerializer, EnderecoSerializer

class ClienteList(APIView):
    """
    Methods HTTP - GET ALL, POST OBJECT
    """
    def get(self, request, format=None):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)

    # post object
    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteMethodObject(APIView):
    """
    Methods HTTP - GET OBJECT DETAIL, PUTH, DELETE
    """
    # get object
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    # get object or all
    def get(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    # put object
    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EnderecoList(APIView):
    """
    Methods HTTP - GET ALL, POST OBJECT
    """
    def get(self, request, format=None):
        endereco = Endereco.objects.all()
        serializer = EnderecoSerializer(endereco, many=True)
        return Response(serializer.data)

    # post object
    def post(self, request, format=None):
        serializer = EnderecoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnderecoMethodObject(APIView):
    """
    Methods HTTP - GET OBJECT DETAIL, PUTH, DELETE
    """
    # get object
    def get_object(self, pk):
        try:
            return Endereco.objects.get(pk=pk)
        except Endereco.DoesNotExist:
            raise Http404

    # get object
    def get(self, request, pk, format=None):
        endereco = self.get_object(pk)
        serializer = EnderecoSerializer(endereco)
        return Response(serializer.data)

    # put object
    def put(self, request, pk, format=None):
        endereco = self.get_object(pk)
        serializer = EnderecoSerializer(endereco, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete object
    def delete(self, request, pk, format=None):
        endereco = self.get_object(pk)
        endereco.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
