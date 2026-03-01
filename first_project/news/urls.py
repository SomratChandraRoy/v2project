from django.urls import path
from .views import (
    home,
    detail_news,
    news_api,
    news_get_or_create,
    news_detail,
    NewsRetrieveUpdateDestroyView,
    NewsViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"news", NewsViewSet, basename="news")

urlpatterns = [
    path("", home, name="home"),
    path("details/<int:pk>/", detail_news, name="detail_news"),
    path("api/news/", news_get_or_create, name="news_get_or_create"),
    path(
        "api/news/<int:pk>/",
        NewsRetrieveUpdateDestroyView.as_view(),
        name="news_detail",
    ),
] + router.urls
