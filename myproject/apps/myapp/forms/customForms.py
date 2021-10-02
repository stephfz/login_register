from django import forms
from ..models import User

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField( widget= forms.PasswordInput, required=True)

    # def login(self):
    #     email = self.cleaned_data.get('email') 
    #     password = self.cleaned_data.get('password')
    #     user = User.authenticate(email, password) 
    #     if user == None:
    #         print("==== Failed Authentication ====") 
    #         raise forms.ValidationError("Constraseña Incorrecta")    
    #     return user 

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.authenticate(email, password)
        if user == None:
            raise forms.ValidationError("Datos no válidos")