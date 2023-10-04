from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Email Address",
        }
        widgets = {
            "text": forms.Textarea(attrs={'rows': 4, 'cols': 50}),
        }
