from django.shortcuts import render
from .models import News
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsSerializer, NewsCreateSerializer
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from rest_framework.viewsets import ModelViewSet


# Create your views here.
def home(request):
    all_news = News.objects.all()
    return render(request, "home.html", {"news": all_news, "len": len(all_news)})


def detail_news(request, pk):
    news = News.objects.get(id=pk)
    return render(request, "detail.html", {"news": news})


def news_api(request):
    all_news = News.objects.all()
    response = {"news": []}
    for news in all_news:
        response["news"].append(
            {
                "title": news.title,
                "banner": news.banner.url,
                "content": news.content,
                "created_time": news.created_time,
                "updated_time": news.updated_time,
                "author": {
                    "name": news.author.username,
                    "id": news.author.id,
                    "bio": news.author.bio,
                    "image": news.author.image.url,
                    "subtitle": news.author.subtitle,
                },
            }
        )
    return JsonResponse(response)


# Function Based Views Django Rest Framework
@api_view(["GET", "POST"])
def news_get_or_create(request):
    if request.method == "GET":
        all_news = News.objects.all()
        serializer = NewsSerializer(all_news, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = NewsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def news_detail(request, pk):
    try:
        news = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response({"message": "News not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = NewsSerializer(news)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        news.delete()
        return Response({"message": "News deleted"}, status=status.HTTP_204_NO_CONTENT)
    if request.method == "PUT":
        serializer = NewsSerializer(news, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class Based Views Django Rest Framework


class NewsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsListCreateAPIView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


# Viewset Django Rest Framework


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
