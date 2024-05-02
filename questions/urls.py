from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.QuestionsCreateListView.as_view(), name='questions-create-list'),
    path('questions/<int:pk>/', views.QuestionsUpdateDestroyView.as_view(), name='questions-detail-view'),
]