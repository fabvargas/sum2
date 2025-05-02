from rest_framework import serializers
from core.models import UserProfile, Sells

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sells
        fields = '__all__'
