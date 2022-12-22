from django.urls import path
from payments.views import OutstandingView, PrincipalOutstandingView, ForeclosureAmountView, BBPSPaymentView

urlpatterns = [
    path('get-outstanding/', OutstandingView.as_view()),
    path('get-principal-outstanding/', PrincipalOutstandingView.as_view()),
    path('get-foreclosure-amount/', ForeclosureAmountView.as_view()),
    path('bbps/', BBPSPaymentView.as_view())
]