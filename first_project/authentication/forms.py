from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Author


class AuthorSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = Author
        fields = (
            "image",
            "username",
            "email",
            "subtitle",
            "bio",
            "password1",
            "password2",
        )
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Choose a username"}),
            "subtitle": forms.TextInput(attrs={"placeholder": "e.g. Tech Journalist"}),
            "bio": forms.Textarea(attrs={"placeholder": "Tell us about yourself...", "rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"placeholder": "your@email.com"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Create a password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm password"})
