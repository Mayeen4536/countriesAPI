from rest_framework import serializers

from contriesapi.models import Contries


class ContriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contries
        fields = ('id', 'name', 'capital')
