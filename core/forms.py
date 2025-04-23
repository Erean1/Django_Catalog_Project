from django import forms
from .models import Film_Post,Comment

class FilmPostForm(forms.ModelForm):
    class Meta:
        model = Film_Post
        fields = ['title','director','description','image','publication_date','category']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']