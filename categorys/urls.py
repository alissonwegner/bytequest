from django.urls import path
from . import views

urlpatterns = [
    path('categorys/', views.CategorysCreateListView.as_view(), name='categorys-create-list'),
    path('categorys/<int:pk>/', views.CategorysUpdateDestroyView.as_view(), name='categorys-detail-view'),
]