from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FavoriteCrypto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto_id = models.CharField(max_length=100)  # CoinGecko ID
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.user.username})"