from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creado_por = models.CharField("Creado por", max_length=50, blank=True)

    def __str__(self):
        return "Perfil"
@receiver(post_save, sender=User)
def create_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    else:
        if hasattr(instance, "perfil") and instance.is_staff:
            instance.perfil.creado_por = "ADMIN_MASTER"
            instance.perfil.save()


def pathArchivo(instance, filename):
    actividad = instance.activ
    creacion = instance.creacion.strftime("%Y-%m-%d_%H-%M")
    filearr = filename.split(".")
    extension = filearr[len(filearr)-1]
    return 'Uploads/{0}/{1}/{2}'.format(instance.user.username, actividad, "{0}.{1}".format(creacion, extension))
class Actividad(models.Model):
    user = models.ForeignKey(User, related_name="actividades", on_delete=models.CASCADE)
    activs_choices = [
        ("Actividad_Uno", "Actividad Uno"),
        ("Actividad_Dos", "Actividad Dos"),
        ("Actividad_Tres", "Actividad Tres"),
        ("Actividad_Cuatro", "Actividad Cuatro"),
        ("Actividad_Cinco", "Actividad Cinco")
    ] 
    activ = models.CharField("Actividad", max_length=20, choices=activs_choices)
    comentario = models.CharField("Comentario", max_length=500)
    creacion = models.DateTimeField("Creacion", default=now)      
    archivo = models.FileField(upload_to=pathArchivo)
