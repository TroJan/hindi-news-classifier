from django import forms


class TokenizeForm(forms.Form):

    text = forms.CharField(
        label='Input Text',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter text to tokenize',
            'rows':6
        })
    )
