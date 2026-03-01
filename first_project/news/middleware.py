from .models import Page


class ViewCounterMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        print("View counter middleware")

        page = Page.objects.get_or_create(url=request.path)
        page[0].views += 1
        page[0].save()
        request.page_views = page[0].views
        print(request.page_views)
        response = self.get_response(request)

        return response
