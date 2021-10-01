from django import forms
from django.forms.widgets import ClearableFileInput

from ..models import User

my_default_errors = {
    'required': 'Requerido',
    'invalid': 'Correo Invalido'
    
}

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label = 'Confirmar Contraseña'
    )
    email = forms.EmailField(required=True, label= "Correo Electronico", error_messages= my_default_errors)

    class Meta:
        model = User
        fields = ['name','lastname','email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder': 'Nombres Completos'}),
            'password' : forms.PasswordInput(),
        }
        labels = {
           'name': "Nombres",
           'lastname': "Apellidos",
           'email': "Correo Electronico",
        }

    def clean(self):
        cleaned_data = super(UserForm,self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        print ('email', cleaned_data.get("email"))
        if (password != confirm_password):
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )  
        user_exists = User.user_exists(cleaned_data.get("email"))
        if user_exists:
            raise forms.ValidationError("El usuario ya existe")