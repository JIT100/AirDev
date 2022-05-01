from django.urls import path,include
from .api import RegisterApi,SignoutApi
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt import views as jwt_views
urlpatterns=[
    path('signup', RegisterApi.as_view(),name='register'),
    path('signin', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signin-refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify', TokenVerifyView.as_view(), name='token_verify'),
    path('signout', SignoutApi.as_view()),
]