from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from getpass import getpass

class Command(BaseCommand):
    def handle(self, *args, **options):
        def passfunc(contrasena):
            while True :
                cont = getpass("Password (otra vez): ")
                if contrasena == cont:
                    return cont
                else:
                    print("Los passwords no coinciden")
                    continue

        admin = {
            "username" : input("Username: "),
            "password" : passfunc(getpass("Password: "))
        }
        administrador = User.objects.create_user(
            admin['username'],
            "",
            admin['password']
        )
        administrador.is_staff = True
        administrador.is_superuser = True
        administrador.first_name = input("Nombre: ")
        administrador.last_name = input("Apellido: ")
        administrador.email = input("E-mail: ")
        administrador.save()