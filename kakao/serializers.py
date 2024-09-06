from rest_framework import serializers
from .models import Kakao, KakaoToken


class KakaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kakao
        fields = '__all__'

    def create(self, validated_data):
        return Kakao.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    def delete(self, instance, validated_data):
        pass


class KakaoTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KakaoToken
        fields = '__all__'

    def create(self, validated_data):
        return KakaoToken.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    def delete(self, instance, validated_data):
        pass
