from rest_framework import serializers
from gthockey.models import Player

"""
class PlayerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    position = serializers.CharField(read_only=True)
    number = serializers.IntegerField(read_only=True)
    hometown = serializers.CharField(read_only=True)
    school = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return instance
"""
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'first_name', 'last_name', 'position', 'number', 'hometown', 'school')