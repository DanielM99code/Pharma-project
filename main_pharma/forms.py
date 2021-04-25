from django import forms
from .models import Message


class FormMessage(forms.ModelForm):
    user_fname = forms.CharField(max_length=40,
                                 widget=forms.TextInput(attrs={'type': 'text', 'id': 'c_fname', 'class': 'form-control',
                                                               'name': 'c_fname'}))
    user_lname = forms.CharField(max_length=40,
                                 widget=forms.TextInput(attrs={'type': 'text', 'id': 'c_lname', 'class': 'form-control',
                                                               'name': 'c_lname'}))
    user_email = forms.EmailField(
        widget=forms.TextInput(attrs={'type': 'email', 'id': 'c_email', 'class': 'form-control',
                                      'name': 'c_email', 'placeholder': ''}))

    user_subject = forms.CharField(max_length=40,
                                   widget=forms.TextInput(attrs={'type': 'text', 'id': 'c_subject', 'class': 'form-control',
                                                                 'name': 'c_subject'}))
    user_message = forms.CharField(max_length=400,
                                   widget=forms.Textarea(attrs={'type': 'c_message', 'id': 'c_message', 'class': 'form-control',
                                                                 'rows': '7', 'cols': "30"}))

    class Meta:
        model = Message
        fields = ('user_fname', 'user_lname', 'user_email', 'user_subject', 'user_message')
