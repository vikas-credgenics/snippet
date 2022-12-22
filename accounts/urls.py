from django.urls import path
from accounts.views import AccountManagement


urlpatterns = [
    path('', AccountManagement.as_view())
]