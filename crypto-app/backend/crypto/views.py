import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FavoriteCrypto
from .serializers import FavoriteCryptoSerializer

class CryptoListView(APIView):
    def get(self, request):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 20,
            'page': 1
        }
        response = requests.get(url, params=params)
        return Response(response.json())

class FavoriteCryptoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        favorite = FavoriteCrypto.objects.create(
            user=request.user,
            crypto_id=data['id'],
            name=data['name'],
            symbol=data['symbol']
        )
        return Response({'message': 'Added to favorites'}, status=201)

    def get(self, request):
        favorites = FavoriteCrypto.objects.filter(user=request.user)
        serializer = FavoriteCryptoSerializer(favorites, many=True)
        return Response(serializer.data)