from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", required=True ,max_length=200)
    check = forms.BooleanField(required=False)