from .models import Cheese
from rest_framework import serializers

## Serializer Class
class CheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # the model it will serialize
        model = Cheese
        # the fields that should be included in the serailized output
        fields = ['id', 'name', 'origin_country', 'type']