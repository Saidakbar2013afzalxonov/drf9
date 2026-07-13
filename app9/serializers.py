from rest_framework import serializers
from .models import Phones

class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['id', 'name', 'price', 'description', 'created_year', 'created_at']
        read_only_fields = ['id', 'created_at']