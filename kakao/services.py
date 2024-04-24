import json

import requests

from admin.settings import SOCIAL_OUTH_CONFIG


class KakaoServices(object):

    def get_token(self, code):
        print(f"코드 : {code}")
        access_token = requests.post(
            "https://kauth.kakao.com/oauth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "authorization_code",
                "client_id": SOCIAL_OUTH_CONFIG["KAKAO_REST_API_KEY"],
                "redirect_uri": SOCIAL_OUTH_CONFIG["KAKAO_REDIRECT_URI"],
                'client_secret': SOCIAL_OUTH_CONFIG['KAKAO_SECRET_KEY'],
                "code": code
            },
        )
        print(access_token)
        if access_token.status_code == 400 :
            return access_token.json()['error']
        else:
            access_token = access_token.json()['access_token']
            print(f" access_token ====== {access_token}")
            return access_token

    def get_kakao_user(self, access_token):
        user_data = requests.get(
            "https://kapi.kakao.com/v2/user/me",
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
            },
        )
        print(user_data.status_code)
        if user_data.status_code == 401 :
            print(user_data.json())
            return user_data.json()
        else:
            user_data = user_data.json()
            print(f'user data =====  {user_data}')
            kakao_account = user_data['kakao_account']
            profile = kakao_account['profile']
            print(profile)
            email = kakao_account['email']
            nickname = profile['nickname']
            kakao_user = {'id': email, 'nickname': nickname}
            return kakao_user
