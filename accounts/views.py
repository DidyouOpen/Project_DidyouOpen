from django.shortcuts import render, redirect
from .models import User
from django.conf import settings
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
import requests
from django.contrib.auth import login

BASE_URL = 'http://127.0.0.1:8000/'


def kakao_login(request):
    rest_api_key =  getattr(settings, 'KAKAO_REST_API_KEY')
    redirect_uri = BASE_URL + "accounts/kakao/callback/"
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={redirect_uri}&response_type=code"
    )

class KaKaoException(Exception):
    pass


def kakao_callback(request):
    try:
        rest_api_key =  getattr(settings, 'KAKAO_REST_API_KEY')
        redirect_uri = BASE_URL + "accounts/kakao/callback/" ##callback
        code = request.GET.get("code") ## code
        token_request = requests.get(f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
        token_request_json = token_request.json()
        error = token_request_json.get("error")
        if error is not None:
            raise KaKaoException()
        access_token = token_request_json.get("access_token")
        profile_request = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization" : f"Bearer {access_token}"})
        profile_json = profile_request.json()
        properties = profile_json.get('properties')
        kakao_account = profile_json.get('kakao_account')
        profile = kakao_account.get("profile")
        nickname = profile.get("nickname")

        data = {'access_token' : access_token, 'code' : code}
        accept = requests.post(
            f"{BASE_URL}accounts/kakao/login/finish/", data=data
        )
        accept_json = accept.json()
        accept_user = accept_json.get("user")
        pk = accept_user.get("pk")
        try:        
            user = User.objects.get(pk=pk)
            User.objects.filter(pk=pk).update(nickname=nickname)
        except KaKaoException:
            return redirect('/error_user/')
        login(
            request,
            user,
            backend="django.contrib.auth.backends.ModelBackend",
            )
        
        return redirect ('/')

    except KaKaoException:
        return redirect('/signin/')


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = BASE_URL + "accounts/kakao/callback/"