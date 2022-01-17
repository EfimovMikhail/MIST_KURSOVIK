from rest_framework import serializers

from .models import Merop

class MeropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merop
        fields = ('name', 'participants', 'date', 'place', 'description', 'published')
