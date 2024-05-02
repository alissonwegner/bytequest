from rest_framework import serializers
from options.models import Options


class OptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Options
        fields = '__all__'
        #__all__ quer dizer que pode usar todos