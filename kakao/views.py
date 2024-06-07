import jwt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from kakao.services import KakaoServices
from kakao.serializers import KakaoSerializer, KakaoTokenSerializer
from kakao.repositories import KakaoRepository


@api_view(['POST'])
def kakao_login(request):
    try:
        print(f"a = {request.data}")
        code = request.data["code"]
        get_token = KakaoServices().get_token(code)
        if get_token == 'invalid_grant':
            return Response({'data': 'not found token'})
        else:
            kakao_user = KakaoServices().get_kakao_user(get_token)
            token = KakaoRepository().get_jwt(kakao_user)
            if KakaoRepository().find_kakao_exists(kakao_user['id']) is not False:
                kakaoTokenSerializer = KakaoTokenSerializer(data=token)
                if kakaoTokenSerializer.is_valid():
                    kakaoTokenSerializer.save()
                    print('kakaoToken 저장')
                    return Response(kakaoTokenSerializer.data, status=status.HTTP_201_CREATED)
                else:
                    print('kakaoToken 저장중 에러')
                    return Response(kakaoTokenSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                kakaoSerializer = KakaoSerializer(data=kakao_user)
                if kakaoSerializer.is_valid():
                    kakaoSerializer.save()
                    print(f'kakao 정보 저장된 데이터 ::::: {kakaoSerializer.data}')
                    kakaoTokenSerializer = KakaoTokenSerializer(data=token)
                    if kakaoTokenSerializer.is_valid():
                        kakaoTokenSerializer.save()
                        print('kakaoToken 저장')
                        return Response(kakaoTokenSerializer.data, status=status.HTTP_201_CREATED)
                    else:
                        print('kakaoToken 저장중 에러')
                        return Response(kakaoTokenSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(kakaoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET '])
def kakao_token(request):
    if request.method == "POST":
        token = KakaoRepository().get_jwt(request.data['id'])
        serializer = KakaoTokenSerializer(data=token)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else : return KakaoRepository().get_all_kakao_token()


@api_view(['GET'])
def kakao_get_all(request):
    return KakaoRepository().get_all_kakao()


@api_view(['GET'])
def kakao_token_get_all(request):
    return KakaoRepository().get_all_kakao_token()
