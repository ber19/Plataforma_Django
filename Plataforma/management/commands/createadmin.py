from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from getpass import getpass
import re

class Command(BaseCommand):
    def handle(self, *args, **options):

        def passFunc():
            while True:
                contrasena = getpass("Password: ").strip()
                cont= getpass("Password (otra vez): ").strip()
                if contrasena == cont:
                    return cont
                else:
                    print("Las contraseñas no coinciden. Vuelve a intentarlo")
                    continue
        def valEmail():
            while True:
                email = input("E-mail: ")
                regex = re.search("^\w+([\.-]?\w+)+@\w+([\.:]?\w+)+(\.[a-zA-Z0-9]{2,3})+$", email)
                if regex:
                    return email
                else:
                    print("Ingrese un email valido")
                    continue

        admin = {
            "username" : input("Username: ").strip(),
            "password" : passFunc()
        }
        try:
            administrador = User.objects.create_user(
                admin['username'],
                "",
                admin['password']
            )
            administrador.is_staff = True
            administrador.is_superuser = True
            administrador.first_name = input("Nombre: ").strip()
            administrador.last_name = input("Apellido: ").strip()
            administrador.email = valEmail()
            administrador.save()
        except:
            print("---El usuario ya existe---")

        
