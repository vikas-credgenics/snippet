from django.urls import path

from . import views

urlpatterns = [
    # url(r'^v1/', include(v1)),
    # url(r'^v2/', include(v2)),
    path('person/', views.PersonListV1.as_view()),
]