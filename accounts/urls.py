from django.urls import path
from .views.account_management import AccountManagement


urlpatterns = [
    path('', AccountManagement.as_view())
]