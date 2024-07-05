from datetime import datetime

import jwt
import requests

from admin.settings import SOCIAL_AUTH_CONFIG


class KakaoServices(object):

    def get_token(self, code):
        print(f"코드 : {code}")
        access_token = requests.post(
            "https://kauth.kakao.com/oauth/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={
                "grant_type": "authorization_code",
                "client_id": SOCIAL_AUTH_CONFIG["KAKAO_REST_API_KEY"],
                "redirect_uri": SOCIAL_AUTH_CONFIG["KAKAO_REDIRECT_URI"],
                'client_secret': SOCIAL_AUTH_CONFIG['KAKAO_SECRET_KEY'],
                "code": code
            },
        )
        print(access_token)
        if access_token.status_code == 400:
            error_message = access_token.json()['error_description']
            print(f"Error fetching access token: {error_message}")
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
        if user_data.status_code == 401:
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

    def get_jwt(self, user_info):
        dt = str(datetime.now())
        encoded_jwt = jwt.encode({'id': user_info['id'], 'nickname': user_info['nickname'], 'datetime': dt},
                                 SOCIAL_AUTH_CONFIG['KAKAO_SECRET_KEY'], algorithm=SOCIAL_AUTH_CONFIG['ALGORITHM'])
        kakao_token = {"token": encoded_jwt, 'id': user_info['id']}
        payload = jwt.decode(encoded_jwt, SOCIAL_AUTH_CONFIG['KAKAO_SECRET_KEY'],
                             algorithms=SOCIAL_AUTH_CONFIG['ALGORITHM'])
        print(payload)
        return kakao_token
