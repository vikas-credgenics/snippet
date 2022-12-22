from django.urls import path
from payments.views import OutstandingView

urlpatterns = [
    path('get-outstanding/', OutstandingView.as_view())
]