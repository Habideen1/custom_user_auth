from django.urls import path
from .views import RegisterAPIView


urlpatterns = [
    path("api/vi/auth/register", RegisterAPIView.as_view(), name="register"),
]


