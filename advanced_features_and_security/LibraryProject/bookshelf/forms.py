from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)

class ExampleForm(forms.Form):
    """
    Example form for demonstration.
    """
    name = forms.CharField(max_length=100, required=True, label='Your Name')
    email = forms.EmailField(required=True, label='Your Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Your Message')
