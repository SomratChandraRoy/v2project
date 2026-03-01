from django.shortcuts import render, redirect
from .forms import AuthorSignupForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.generics import CreateAPIView
from .serializers import AuthorSignupSerializer


# Create your views here.
def signup(request):
    if request.POST:
        form = AuthorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "signup.html", {"form": form})
    else:
        form = AuthorSignupForm()
        return render(request, "signup.html", {"form": form})


# Login View API


@api_view(["POST"])
def login_api(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    print(f"Attempting login with username: {username} and password: {password}")
    print(f"Authenticated user: {user}")

    if user is not None:
        login(request, user)
        return Response({"message": "Login Successful"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_403_FORBIDDEN
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout_api(request):
    logout(request)
    return Response({"message": "Logout Successful"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def whoami(request):
    return Response(
        {"username": request.user.username, "id": request.user.id},
        status=status.HTTP_200_OK,
    )


class SignupAPI(CreateAPIView):
    serializer_class = AuthorSignupSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response(
            {"message": "User created successfully"}, status=status.HTTP_201_CREATED
        )
