from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from categorys.views import category_view

def hello_view(request):
    return JsonResponse({'message': 'hello world!'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('categorys/', category_view, name='categorys-list'),
]

