from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView 
from accounts import models
import environ
from rest_framework import authentication, permissions
env = environ.Env()
environ.Env.read_env()

# @api_view(['POST',])
# def logout_view(request):

#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)

class logout_view(GenericAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        User =  request.user
        created = Token.objects.get(user=User)
        created.delete()
        return Response(status=status.HTTP_200_OK)


from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

class CreateTokenView(GenericAPIView):

    # permission_classes = [IsAuthenticated]
    # serializer_class = MediaBucketSerializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        User = get_user_model()
        user = User.objects.filter(email=email).first()

        if user is not None and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'detail': 'Invalid credentials'}, status=401)


from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Account

class ForgotPasswordView(GenericAPIView):
    def post(self, request):
        email = request.data.get('email')
        print(email)

        User = get_user_model()
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)

            # Reset password email
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            backendurl = env("BACKEND_URL")
            
            # Compose password reset email
            subject = 'Reset Your Password'
            message = f"Click the following link to reset your password:\n\n" \
                      f"backendurl/{uid}/{token}\n\n" \
                      f"If you didn't request this, please ignore this email."
            to_email = email
            send_email = EmailMessage(subject, message, to=[to_email])
            send_email.send()

            return Response({'detail': 'Password reset email has been sent to your email address.'})
        else:
            return Response({'detail': 'Account does not exist!'}, status=status.HTTP_404_NOT_FOUND)


from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework.views import APIView

class ResetPasswordValidateView(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            User = get_user_model()
            user = User._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            request.session['uid'] = uid
            return Response({'detail': 'please reset your password!'})
        else:
            return Response({'detail': 'This link has expired!'}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class ResetPasswordView(GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request):
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if password == None or confirm_password == None:
            return Response({'detail': 'Please enter a password and confirm password.'}, status=status.HTTP_400_BAD_REQUEST)

        if password == confirm_password:
            uid = request.session.get('uid')
            User = get_user_model()
            user = User.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            return Response({'detail': 'Password reset successful'})
        else:
            return Response({'detail': 'Passwords do not match!'}, status=status.HTTP_400_BAD_REQUEST)




# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate, login
# from rest_framework.authtoken.models import Token

# class UserLoginAPIView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(request, email=email, password=password)
#         print(user);
#         if user is not None:
#             login(request, user)
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key, 'message': 'You are now logged in.'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# from rest_framework.authtoken.models import Token
# from rest_framework.authtoken.serializers import AuthTokenSerializer
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class UserLoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = AuthTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)

#         token, _ = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key, 'detail': 'You are now logged in.'})
