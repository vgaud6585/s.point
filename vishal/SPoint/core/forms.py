from django import forms

class StudyRecapForm(forms.Form):
    heading = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter topic heading...'})
    )
    # Form mein TextField nahi, CharField + Textarea widget hota hai
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'What did you learn?'})
    )
    code_snippet = forms.CharField(
        required=False, # Agar code optional rakhna ho
        widget=forms.Textarea(attrs={'rows': 6, 'placeholder': 'Paste your code here...'})
    )
