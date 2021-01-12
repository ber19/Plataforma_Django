from django.contrib import admin
from django.urls import path, include
from Plataforma.views import *
from rest_framework import routers
from Plataforma.api import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuariosViewSet)
router.register(r'actividades/(?P<id>[0-9]+)', views.ActividadesViewSet, basename="actividades")
router.register(r'newactividad', views.NewActividadViewSet, basename="newactividad")

urlpatterns = [
    path("", loginView, name="login"),
    path("admin/", adminView, name="admin"),
    path("user/", userView, name="user"),
    path("logout/", logoutView, name="logoutView"),
    path("users/", usersView, name="usersView"),
    path("new_user/", newUserView, name="newUserView"),
    path("edit_user/<int:id>", editUserView, name="editUserView"),
    path("cambiar_cont/<int:id>", cambiarContView, name="cambiarContView"),
    path("del_user/<int:id>", deleteUser, name="deleteUserView"),
    path("new_activ/<int:id>", newActView, name="newActView"),
    path("actividades/<int:id>", activsUserView, name="activsUserView"),
    #--------API----------#
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework"))

]