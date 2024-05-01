from django.shortcuts import render
from django.http import JsonResponse
from categorys.models import Categorys
from rest_framework import generics
from categorys.serializers import CategorysSerializer


class CategorysCreateListView(generics.ListCreateAPIView):
    queryset = Categorys.objects.all()
    serializer_class = CategorysSerializer

class CategorysUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorys.objects.all()
    serializer_class = CategorysSerializer
