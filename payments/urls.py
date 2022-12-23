from django.urls import path
from payments.views import BBPSPaymentView, GetLoanAmount

urlpatterns = [
    path('get-amount/', GetLoanAmount.as_view()),
    path('bbps/', BBPSPaymentView.as_view())
]