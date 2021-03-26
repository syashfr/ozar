from django import forms
from .models import Design

class UploadForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ('name', 'type', 'description', 'file', 'tags', 'image' )