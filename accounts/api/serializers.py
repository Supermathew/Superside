from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'   
        # extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):

    blogthumbnailimg_path = serializers.SerializerMethodField()

    def get_blogthumbnailimg_path(self, obj):
        if obj.profiledp:
            return obj.profiledp.image.url
        return None
    class Meta:
        model = UserProfile
        fields = '__all__'   
