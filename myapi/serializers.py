from rest_framework import serializers

from .models import Merop

class MeropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merop
        fields = ('name', 'participants', 'date', 'place', 'description')
