from django.shortcuts import render, redirect
from .forms import NewsForm
from news.models import News
from authentication.models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import RetrieveAPIView
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.


class AuthorRetrieve(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


def news_create(request):
    if request.user.is_authenticated:
        if request.POST:
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news = form.save(commit=False)
                news.author = request.user
                news.save()
                return redirect("detail_news", pk=news.id)
            else:
                return render(request, "news_form.html", {"form": form})
        else:
            form = NewsForm()
            return render(request, "news_form.html", {"form": form})
    else:
        return redirect("login")


def delete_news(request, pk):
    if request.user.is_authenticated:
        news = News.objects.get(id=pk)
        if news.author == request.user:
            news.delete()
            return redirect("home")

        else:
            return redirect("login")
    else:
        return redirect("login")


def news_update(request, pk):
    if request.user.is_authenticated:
        news = News.objects.get(id=pk)
        if news.author == request.user:
            if request.POST:
                form = NewsForm(request.POST, request.FILES, instance=news)
                if form.is_valid():
                    form.save()
                    return redirect("detail_news", pk=news.id)
            else:
                form = NewsForm(instance=news)
                return render(request, "news_form.html", {"form": form})
        else:
            return redirect("login")
    else:
        return redirect("login")
