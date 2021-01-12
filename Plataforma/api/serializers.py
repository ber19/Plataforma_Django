from rest_framework import serializers
from django.contrib.auth.models import User
from Plataforma.models import Actividad
from datetime import datetime
from django.utils.timezone import now

class UsuarioSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        nombre = validated_data["first_name"]
        apellido = validated_data["last_name"]
        email = validated_data["email"]
        newUser = User.objects.create_user(
            username,
            email,
            password
        ) 
        newUser.first_name = nombre
        newUser.last_name = apellido
        newUser.perfil.creado_por = self.context["request"].user.username
        newUser.save()
        newUser.perfil.save()
        return newUser

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name",
                "last_name", "is_staff", "password")

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ("activ", "comentario", "creacion", "archivo", "user_id")


class NewActividadSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        activ = validated_data["activ"]
        comentario = validated_data["comentario"]
        archivo = validated_data["archivo"]
        ahora = now().strftime("%d/%m/%Y %H:%M:%S")
        creacion = datetime.strptime(ahora, "%d/%m/%Y %H:%M:%S")
        user_id = self.context["request"].user.id
        newActiv = Actividad.objects.create(activ=activ, comentario=comentario,
                                            archivo=archivo, user_id=user_id, creacion=creacion)
        return newActiv

    class Meta:
        model = Actividad
        fields = ("activ", "comentario", "creacion", "user_id", "archivo")
