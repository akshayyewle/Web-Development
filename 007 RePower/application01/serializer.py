from rest_framework import serializers
from application01.models import Model01

class Model01_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Model01
        fields = ('id', 'Field01', 'Field02', 'Field03', 'Field04', 'Field05', 'Field06')