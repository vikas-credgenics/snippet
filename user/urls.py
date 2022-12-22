from django.urls import path
from django.conf import settings
from .views import Register, Login, Logout, DocumentView
from django.conf.urls.static import static

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('document/', DocumentView.as_view())
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)