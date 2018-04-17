from django import forms

class FirstForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))
    icq = forms.CharField(max_length=60, required=False)
    count = forms.DecimalField(max_digits=10, decimal_places=6)
    code = forms.CharField(max_length=60, required=False)