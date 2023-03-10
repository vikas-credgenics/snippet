from django.urls import path
from .views import RewardWalletBalance, RewardWalletEarnAPI, RewardWalletBurnAPI, RewardLoadAPI, RewardWalletTransaction


urlpatterns = [
    path('balance/', RewardWalletBalance.as_view()),
    path('transaction/', RewardWalletTransaction.as_view()),
    path('earn/', RewardWalletEarnAPI.as_view()),
    path('burn/', RewardWalletBurnAPI.as_view()),
    path('load/', RewardLoadAPI.as_view())
]
