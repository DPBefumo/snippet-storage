from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    
    
    class Meta:
        # tags = 
        
        model = Snippet
        fields = [
            'title',
            'language',
            'description',
            'body',
            'tags',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'pa2 f4 w-100 bg-silver'}),
            'language': forms.TextInput(attrs={'class': 'pa2 f4 w-100 bg-silver'}),
            'description': forms.TextInput(attrs={'class': 'pa2 f4 w-100 bg-silver'}),
            'body': forms.Textarea(attrs={'class': 'pa2 f4 h4 w-100 bg-silver'}),
        } 