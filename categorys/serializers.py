from rest_framework import serializers
from categorys.models import Categorys


class CategorysSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorys
        fields = '__all__'
        #__all__ quer dizer que pode usar todos