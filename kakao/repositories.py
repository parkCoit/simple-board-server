from datetime import datetime

import jwt
from django.http import JsonResponse
from rest_framework.response import Response

from admin.settings import SOCIAL_AUTH_CONFIG
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

    def get_jwt(self, user_info):
        dt = str(datetime.now())
        encoded_jwt = jwt.encode({'id': user_info['id'], 'nickname': user_info['nickname'], 'datetime': dt},
                                 SOCIAL_AUTH_CONFIG['KAKAO_SECRET_KEY'], algorithm=SOCIAL_AUTH_CONFIG['ALGORITHM'])
        kakao_token = {"token": encoded_jwt, 'id' : user_info['id']}
        payload = jwt.decode(encoded_jwt, SOCIAL_AUTH_CONFIG['KAKAO_SECRET_KEY'],
                             algorithms=SOCIAL_AUTH_CONFIG['ALGORITHM'])
        print(payload)
        return kakao_token
