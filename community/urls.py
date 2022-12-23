from django.urls import path
from community.views import VendorList, VendorDetail, TestimonialView

urlpatterns = [
    path('vendor/', VendorList.as_view()),
    path('vendor/<pk>/', VendorDetail.as_view()),
    path('vendor/<pk>/testimonial/', TestimonialView.as_view())
]