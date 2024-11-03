from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(),
        required=False
    )

    class Meta:
        model = ArticleImage
        fields = ['images']
