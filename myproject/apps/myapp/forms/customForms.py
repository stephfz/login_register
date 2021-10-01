from django import forms
from ..models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField( widget= forms.PasswordInput, required=True)

    def login(self):
        email = self.cleaned_data.get('email') 
        password = self.cleaned_data.get('password')
        user = User.authenticate(email, password) 
        if user == None:
            print("==== Failed Authentication ====") 
            raise forms.ValidationError("Constraseña Incorrecta")    
        return user 

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        user_exist = User.user_exists(email)
        if not user_exist:
            raise forms.ValidationError("Usuario no Existe")    