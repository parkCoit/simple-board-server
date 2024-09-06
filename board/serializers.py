from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

    def create(self, validated_data):
        return Board.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Board.objects.filter(title=validated_data['old_title'], author=validated_data['author']).update(
            title=validated_data['new_title'],
            content=validated_data['new_content'])

    def delete(self, instance, validated_data):
        pass
