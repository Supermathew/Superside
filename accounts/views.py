from django.shortcuts import render

# Create your views here.

from rest_framework.authtoken.models import Token

def create_token(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})
