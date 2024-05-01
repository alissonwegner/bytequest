from django.urls import path
from . import views

urlpatterns = [
    path('categorys/', views.GenreCreateListView.as_view(), name='genre-create-list'),
    path('categorys/<int:pk>/', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
]