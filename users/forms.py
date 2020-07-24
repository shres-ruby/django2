from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import User, Image

USER = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email','first_name','last_name','password1','password2')

    def clean_email(self):
        if USER.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("An account already exists with this email")
        return self.cleaned_data['email']
    
    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
    

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','image']