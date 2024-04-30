from django.shortcuts import render
from django.http import JsonResponse
from categorys.models import Categorys

def category_view(request):
    categorys = Categorys.objects.all()
    data = [{'id': category.category_id, 'texto': category.categoria_txt} for category in categorys]

    return JsonResponse(data, safe=False)