from django.urls import path
from .views import CryptoListView, FavoriteCryptoView

urlpatterns = [
    path('cryptos/', CryptoListView.as_view(), name='crypto-list'),
    path('favorites/', FavoriteCryptoView.as_view(), name='favorite-list'),
    path('favorites/add/', FavoriteCryptoView.as_view(), name='favorite-add'),
]