from news.models import News
from django import forms
from django.forms import ModelForm


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ("title", "banner", "content")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter article title..."}),
            "content": forms.Textarea(
                attrs={"placeholder": "Write your article content here...", "rows": 10}
            ),
        }
