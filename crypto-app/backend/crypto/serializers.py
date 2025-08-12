from rest_framework import serializers
from .models import FavoriteCrypto

class FavoriteCryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteCrypto
        fields = '__all__'