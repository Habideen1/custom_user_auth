from django.urls import path
from .views import RegisterAPIView


urlpatterns = [
    path("api/v1/auth/register", RegisterAPIView.as_view(), name="register"),
]


