from rest_framework.response import Response

from kakao.models import Kakao, KakaoToken
from kakao.serializers import KakaoSerializer, KakaoTokenSerializer


class KakaoRepository(object):

    def __init__(self):
        pass

    def get_all_kakao(self):
        return Response(KakaoSerializer(Kakao.objects.all(), many=True).data)

    def get_all_kakao_token(self):
        return Response(KakaoTokenSerializer(KakaoToken.objects.all(), many=True).data)

    def find_kakao_exists(self, id):
        return Kakao.objects.all().filter(id=id).exists()
