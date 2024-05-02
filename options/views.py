from django.shortcuts import render
from options.models import Options
from rest_framework import generics
from options.serializers import OptionsSerializer


class OptionsCreateListView(generics.ListCreateAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer

class OptionsUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
