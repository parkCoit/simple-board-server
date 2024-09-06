from django.urls import path

from kakao.views import kakao_login, kakao_token, kakao_get_all, kakao_token_get_all

urlpatterns = [
    path('login', kakao_login),
    path('token', kakao_token),
    path('getKakao', kakao_get_all),
    path('getKakaoToken', kakao_token_get_all)
]