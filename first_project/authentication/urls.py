from django.urls import path
from .views import signup, login_api, whoami, logout_api, SignupAPI

urlpatterns = [
    path("", signup, name="signup"),
    path("api/login/", login_api, name="api_login"),
    path("api/signup/", SignupAPI.as_view(), name="signup_api"),
    path("api/logout/", logout_api, name="api_logout"),
    path("api/whoami/", whoami, name="whoami"),
]
