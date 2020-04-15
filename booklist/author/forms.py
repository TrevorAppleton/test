from django import forms
from .models import author

class AuthorForm(forms.Modelform):
    class Meta:
        model = author
    def __init__(self, *args, **kwargs):
        self.fields["listofbooks_pk"] = forms.CharField(widget=forms.HiddenInput())
        super(AuthorForm, self).__init__(self, *args, **kwargs)