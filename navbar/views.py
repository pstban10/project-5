from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from navbar.forms import RegisterForm


# Create your views here.


def inicio(request):
    return render(
        request,
        'base.html'
    )


@login_required
def perfil(request):

    return render(
        request,
        'perfil.html'
    )


def ubicaciones(request):

    return render(
        request,
        'ubicaciones.html'
    )


def contacto(request):

    return render(
        request,
        'contacto.html'
    )


def rutinas(request):
    return render(
        request,
        'rutinas.html'
    )


def registro(request):
    data = {
        'form': RegisterForm()
    }
    if request.method == 'POST':
        formulario = RegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['form'] = formulario
            user = authenticate(
                username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')

    return render(
        request,
        'registration/registro.html',
        data
    )


def acceder(request):

    return render(
        request,
        './registration/login.html'
    )


def salir(request):
    logout(request)

    return redirect('inicio')
