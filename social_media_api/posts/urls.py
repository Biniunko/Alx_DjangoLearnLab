from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from . import views
from .views import LikePostView, UnLikePostView

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns = [
    path("feed/", views.FeedView.as_view(), name="feed"),
]
urlpatterns = [
    path("<int:post_id>/like/", LikePostView.as_view(), name="like_post"),
    path("<int:post_id>/unlike/", UnLikePostView.as_view(), name="unlike_post"),
]
