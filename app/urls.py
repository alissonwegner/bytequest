from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from categorys.views import CategorysCreateListView, CategorysUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorys/', CategorysCreateListView.as_view(), name='categorys-create-list'),
    path('categorys/<int:pk>/', CategorysUpdateDestroyView.as_view(), name='categorys-detail-view'),
    #path('api/v1/', include('categorys.urls')),
]

