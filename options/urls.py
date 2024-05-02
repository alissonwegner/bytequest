from django.urls import path
from . import views

urlpatterns = [
    path('options/', views.OptionsCreateListView.as_view(), name='options-create-list'),
    path('options/<int:pk>/', views.OptionsUpdateDestroyView.as_view(), name='options-detail-view'),
]