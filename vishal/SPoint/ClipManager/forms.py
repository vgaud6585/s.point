from django import forms
from .models import Clips

class ClipsForm(forms.ModelForm):
  class Meta:
    model = Clips
    fields = ['heading', 'code_clip']
    widgets = {
      'heading': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title...'}),
      'code_clip': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Paste your code here...'}),
    }
