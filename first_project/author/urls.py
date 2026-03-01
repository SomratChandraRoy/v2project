from django.urls import path
from .views import news_create, delete_news, news_update, AuthorRetrieve

urlpatterns = [
    path("create/", news_create, name="news_create"),
    path(
        "api/<int:pk>/",
        AuthorRetrieve.as_view(),
        name="author_detail",
    ),
    path("delete/<int:pk>/", delete_news, name="delete_news"),
    path("update/<int:pk>/", news_update, name="news_update"),
]
