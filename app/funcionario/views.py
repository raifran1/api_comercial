from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Setor, Funcionario
from .serializers import SetorSerializer, FuncionarioSerializer

class SetorList(APIView):
    """
    Methods HTTP - GET ALL, POST OBJECT
    """
    def get(self, request, format=None):
        setor = Setor.objects.all()
        serializer = SetorSerializer(setor, many=True)
        return Response(serializer.data)

    # post object
    def post(self, request, format=None):
        serializer = SetorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SetorMethodObject(APIView):
    """
    Methods HTTP - GET OBJECT DETAIL, PUTH, DELETE
    """
    # get object
    def get_object(self, pk):
        try:
            return Setor.objects.get(pk=pk)
        except Setor.DoesNotExist:
            raise Http404

    # get object or all
    def get(self, request, pk, format=None):
        setor = self.get_object(pk)
        serializer = SetorSerializer(setor)
        return Response(serializer.data)

    # put object
    def put(self, request, pk, format=None):
        setor = self.get_object(pk)
        serializer = SetorSerializer(setor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        setor = self.get_object(pk)
        setor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FuncionarioList(APIView):
    """
    Methods HTTP - GET ALL, POST OBJECT
    """
    def get(self, request, format=None):
        funcionario = Funcionario.objects.all()
        serializer = FuncionarioSerializer(funcionario, many=True)
        return Response(serializer.data)

    # post object
    def post(self, request, format=None):
        serializer = FuncionarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FuncionarioMethodObject(APIView):
    """
    Methods HTTP - GET OBJECT DETAIL, PUTH, DELETE
    """
    # get object
    def get_object(self, pk):
        try:
            return Funcionario.objects.get(pk=pk)
        except Funcionario.DoesNotExist:
            raise Http404

    # get object or all
    def get(self, request, pk, format=None):
        funcionario = self.get_object(pk)
        serializer = FuncionarioSerializer(funcionario)
        return Response(serializer.data)

    # put object
    def put(self, request, pk, format=None):
        funcionario = self.get_object(pk)
        serializer = FuncionarioSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        funcionario = self.get_object(pk)
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)