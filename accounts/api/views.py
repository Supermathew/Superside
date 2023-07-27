from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView 
from accounts import models
import environ
from accounts.api.serializers import  UserSerializer
from rest_framework import authentication, permissions
env = environ.Env()
environ.Env.read_env()

from accounts.models import Account,UserProfile
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from accounts.api.serializers import *
from django.contrib.auth import update_session_auth_hash

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
from navigation.api.serializers import MediaBucketSerializer

class CreateTokenView(GenericAPIView):

    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        Account = get_user_model()
        user = Account.objects.filter(email=email).first()
        print(user)

        # # User = get_user_model()
        # # user = User.objects.filter(email=email).first()
    
        # profiledp_info = {}
        # if user.profiledp:
        #     serializer = MediaBucketSerializer(user.profiledp)
        #     profiledp_info = serializer.data

        if user is not None and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            response_data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'token': token.key
        }
            return Response(response_data)
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

    serializer_class = UserSerializer
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

            subject = 'Reset Your Password'
            message = f"Click the following link to reset your password:\n\n" \
                      f"{backendurl}/{uid}/{token}\n\n" \
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

    serializer_class = UserSerializer

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
    serializer_class = UserSerializer

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

from navigation.models import MediaBucket

class updateprofileView(GenericAPIView):


    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # Assuming 'request.user' gives you the username "jaseem"
        try:
            # user = Account.objects.get(username=username)  # Get the Account instance using the username
            profile = UserProfile.objects.get(user=user)  # Filter UserProfile using the Account instance

            serializer = UserProfileSerializer(profile)

            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response({'detail': 'UserProfile not found'}, status=404)

    def post(self, request):
        user = request.user
        print(type(user))
        name = request.data.get('name')
        profiledp = request.data.get('profiledp')

        # Assuming 'profiledp' contains the ID of the related MediaBucket object
        media = MediaBucket.objects.get(id=profiledp)

        user_profile = UserProfile.objects.create(user=user, profiledp=media, name=name)

        # Save the UserProfile instance to the database
        user_profile.save()

        serializer = UserProfileSerializer(user_profile)

        # Return the serialized data as part of the JSON response
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        User =  request.user
        ans = UserProfile.objects.get(user=User)

        ans.name = request.data.get('name')
        profiledp = request.data.get('profiledp')
        media = MediaBucket.objects.get(id=profiledp)
        ans.profiledp = media
        ans.save()
        serializer = UserProfileSerializer(ans)

        return Response(serializer.data, status=status.HTTP_200_OK)



class ChangePasswordView(GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)

                return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Please enter a valid current password.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Password does not match.'}, status=status.HTTP_400_BAD_REQUEST)


