from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from user.apps import UserConfig
from user.views import UserRegistrationAPIView, MyTokenObtainPairView, \
    UserListAPIView

app_name = UserConfig.name

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('', UserListAPIView.as_view(), name='user-list')
]
