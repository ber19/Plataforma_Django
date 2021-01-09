from django import forms
from django.contrib.auth.models import User
from Plataforma.models import Actividad

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "id" : "username",
            "class" : "form-control",
            "placeholder" : "Usuario",
            "required" : True,
            "autofocus" : True,
        })
        self.fields["password"].widget = forms.PasswordInput()
        self.fields["password"].widget.attrs.update({
            "id" : "password",
            "class" : "form-control",
            "placeholder" : "Password",
            "required" : True,
        })

class NewUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    passwordA = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "id" : "username",
            "class" : "form-control",
            "required" : True,
            "autofocus" : True
        })
        self.fields["password"].widget = forms.PasswordInput()
        self.fields["password"].widget.attrs.update({
            "id": "password",
            "class": "form-control",
            "required": True,
        })
        self.fields["passwordA"].widget = forms.PasswordInput()
        self.fields["passwordA"].widget.attrs.update({
            "id" : "passwordA",
            "class" : "form-control",
            "placeholder" : "Confirme contraseña",
            "required" : True,

        })
        self.fields["nombre"].widget.attrs.update({
            "id" : "nombre",
            "class" : "form-control",
            "required" : True
        })
        self.fields["apellido"].widget.attrs.update({
            "id" : "apellido",
            "class" : "form-control",
            "required" : True
        })
        self.fields["email"].widget = forms.EmailInput()
        self.fields["email"].widget.attrs.update({
            "id" : "email",
            "class" : "form-control",
            "reuired" : True
        })

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "id": "username",
            "class": "form-control",
            "required": True,
            "readonly" : True
        })
        self.fields["first_name"].widget.attrs.update({
            "id": "first_name",
            "class": "form-control",
            "required": True,
            "autofocus": True
        })
        self.fields["last_name"].widget.attrs.update({
            "id": "last_name",
            "class": "form-control",
            "required": True
        })
        self.fields["email"].widget.attrs.update({
            "id": "email",
            "class": "form-control",
            "required": True
        })

class NewActForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ("user", "activ", "comentario", "creacion", "archivo")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["activ"].widget.attrs.update({
            "id" : "actividad",
            "class" : "form-control",
            "required" : True,
            "autofocus" : True,
        })
        self.fields["comentario"].widget = forms.Textarea()
        self.fields["comentario"].widget.attrs.update({
            "id" : "comentario",
            "class" : "form-contrl",
            "rows" : 10,
            "cols" : 40 
        })
        self.fields["creacion"].widget.attrs.update({
            "id" : "creacion",
            "class" : "form-control",
            "readonly" : True,
        })
        self.fields["archivo"].widget.attrs.update({
            "id": "archivo",
            "class": "form-control",
            "accept" : ".zip, .rar"
        })
        self.fields['user'].widget = forms.HiddenInput()
        self.fields["user"].widget.attrs.update({
            "id": "user",
            "readonly" : True
        })

