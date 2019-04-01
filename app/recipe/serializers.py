from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serialize the tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_obly_fields = ('id')
