from django import forms
from .models import ArticleImage

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget  = forms.ClearableFileInput()) #видалити attr щоб працбвало attrs={'multiple':True})

    class Meta:
        model = ArticleImage
        fields = '__all__'