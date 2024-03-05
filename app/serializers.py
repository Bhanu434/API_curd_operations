from rest_framework import serializers
from app.models import *

class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'