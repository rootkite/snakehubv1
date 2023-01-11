from django import forms
from main.models import NewsLetterUser


class NewsLetterUserForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetterUser
        fields = "__all__"


