from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from Plataforma.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage

# Create your views here.
def loginView(request):
    if request.method == "GET":
        # print(User.objects.all())
        if request.user.is_authenticated and request.user.is_staff:
            return redirect("admin")
        elif request.user.is_authenticated and not request.user.is_staff:
            return redirect("user")
        else:
            form = LoginForm()
            ctx = {
                "form": form
            }
            return render(request, "login.html", ctx)
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("login")
            else:
                form.add_error("username", "Usuario o contraseña incorrectos")
                ctx = {
                    "form": form
                }
                return render(request, "login.html", ctx)

# ---------------------------------------------------------------------------------------------------------------------

@login_required
def adminView(request):
    if not request.user.is_staff:
        raise PermissionDenied()
    else:
        return render(request, "inicio_admin.html")

@login_required
def usersView(request):
    if not request.user.is_staff:
        raise PermissionDenied()
    else:
        usuarios = User.objects.all()
        ctx = {
            "users": usuarios
        }
        return render(request, "users.html", ctx)

@login_required
def newUserView(request):
    if not request.user.is_staff:
        raise PermissionDenied()
    else:
        if request.method == "GET":
            form = NewUserForm()
            ctx = {
                "form": form
            }
            return render(request, "new_user.html", ctx)
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"].strip()
                password = form.cleaned_data["passwordA"]
                nombre = form.cleaned_data["nombre"]
                apellido = form.cleaned_data["apellido"]
                email = form.cleaned_data["email"]
                try:
                    newUser = User.objects.create_user(
                        username,
                        email,
                        password
                    )
                    newUser.first_name = nombre
                    newUser.last_name = apellido
                    newUser.perfil.creado_por = request.user.username
                    newUser.save()
                    newUser.perfil.save()
                    return redirect("login")
                except:
                    form.add_error("username", "El usuario ya existe")
                    ctx = {
                        "form": form
                    }
                    return render(request, "new_user.html", ctx)

@login_required
def editUserView(request, id):
    if not request.user.is_staff:
        raise PermissionDenied()
    else:
        user = get_object_or_404(User, id=id)
        if user.is_staff and user!=request.user:
            raise PermissionDenied()
        else:
            if request.method == "GET":
                form = EditUserForm(instance=user)
                ctx = {
                    "user" : user,
                    "form" : form
                }
                return render(request, "edit_user.html", ctx)
            if request.method == "POST":
                form = EditUserForm(request.POST, instance=user)
                if form.is_valid():
                    form.save()
                    return redirect("usersView")

@login_required
def cambiarContView(request, id):
    if not request.user.is_staff:
        raise PermissionDenied()
    else:
        user = get_object_or_404(User, id=id)
        if request.method == "GET":
            initials = {
                "username" : user.username
            }
            form = NewUserForm(initial=initials)
            form.fields["username"].widget.attrs.update({
                "disabled" : True
            })
            ctx = {
                "form" : form,
                "user" : user
            }
            return render(request, "cambiar_cont.html", ctx)
        if request.method == "POST":
            form = NewUserForm(request.POST)
            del form.fields["username"]
            del form.fields["nombre"]
            del form.fields["apellido"]
            del form.fields["email"]
            if form.is_valid():
                password = form.cleaned_data["passwordA"]
                user.set_password(password)
                user.save()
                return redirect("editUserView", id=user.id)

@login_required
def deleteUser(request, id):
    if not request.user.is_staff:
        raise PermissionDenied()
    else:
        user = get_object_or_404(User, id=id)
        if user.is_staff:
            raise PermissionDenied()
        else:
            if request.method == "GET":
                return render(request, "delete_user.html", {"user":user})
            if request.method == "POST":
                if request.POST["respuesta"] == "cancelar":
                    return redirect("usersView")
                if request.POST["respuesta"] == "aceptar":
                    user.delete()
                    return redirect("usersView")
                
# ---------------------------------------------------------------------------------------------------------------------

@login_required
def userView(request):
    if request.user.is_staff:
        raise PermissionDenied()
    else:
        return render(request, "inicio_user.html")

@login_required
def newActView(request, id):
    if request.user.is_staff:
        raise PermissionDenied()
    else:
        if request.method == "GET":
            form = NewActForm(initial={ 
                "user": request.user.id 
                })
            ctx = {
                "form" : form
            }
            return render(request, "new_actividad.html", ctx)
        if request.method == "POST":
            form = NewActForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('user')

@login_required
def activsUserView(request, id):
    if request.user.id == id or request.user.is_staff:
        from Plataforma.models import Actividad
        actividades = Actividad.objects.filter(user_id=id)
        ctx = {
            "actividades" : actividades
        }
        return render(request, "actividades.html", ctx)
    else:
        raise PermissionDenied()
    
        
# --------------------------------------------------------------------------------------------------------------------

def logoutView(request):
    logout(request)
    return redirect("login")
