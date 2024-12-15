from django.urls import path, include
from .views import RegisterView, LoginView
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]


router = DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
