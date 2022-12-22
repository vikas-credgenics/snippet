from django.urls import path
from .views.user import Register, Login, Logout
from .views.account_management import AccountManagement

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('account_management', AccountManagement.as_view())
]