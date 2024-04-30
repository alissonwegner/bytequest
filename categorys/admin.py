from django.contrib import admin
from categorys.models import Categorys

@admin.register(Categorys)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'categoria_txt')
# Register your models here.
