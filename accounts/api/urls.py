from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CreateTokenView,ForgotPasswordView,ResetPasswordValidateView,ResetPasswordView


from accounts.api.views import  logout_view

urlpatterns = [
    path('login/', CreateTokenView.as_view(), name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('forgotpassword/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('resetpasswordvalidate/<str:uidb64>/<str:token>/', ResetPasswordValidateView.as_view(), name='reset-password-validate'),
    path('resetpassword/', ResetPasswordView.as_view(), name='reset-password'),


    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

]