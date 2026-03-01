from rest_framework.serializers import ModelSerializer, SerializerMethodField
from news.models import News
from authentication.models import Author


class NewsAuthorSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ["title", "content", "banner", "created_time", "updated_time"]


class AuthorSerializer(ModelSerializer):
    news = SerializerMethodField()

    class Meta:
        model = Author
        fields = ["id", "username", "bio", "subtitle", "image", "news"]

    def get_news(self, obj):
        news = News.objects.filter(author=obj)
        return NewsAuthorSerializer(news, many=True).data
