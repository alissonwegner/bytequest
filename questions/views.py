from django.shortcuts import render
from django.http import JsonResponse
from questions.models import Questions
from rest_framework import generics
from questions.serializers import QuestionsSerializer


class QuestionsCreateListView(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

class QuestionsUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer
