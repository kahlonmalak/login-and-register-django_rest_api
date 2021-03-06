from django.urls import path
from rest_framework_simplejwt import views as jwt_views
# from .views import
from .views import (
    UserRegistrationView,
    UserLoginView,
    ChangePasswordView
)

urlpatterns = [
    path('api/token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    
]