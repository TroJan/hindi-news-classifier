from django import forms


class PreprocessForm(forms.Form):

    text = forms.CharField(
        label='Input Text',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter text here',
            'rows':6
        })
    )
