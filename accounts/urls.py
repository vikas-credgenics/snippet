from django.urls import path
from .views.account_management import AccountManagement


urlpatterns = [
    path('account_management', AccountManagement.as_view())
]