from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your name'
        })
    )
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Leave a comment here'
    }))
