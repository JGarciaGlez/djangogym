from rest_framework import serializers
from .models import Todo


class  TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields= ('id','title','series','weights','created_at')
        read_only_fields=('created_at',)
        