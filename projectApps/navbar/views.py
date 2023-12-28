from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from ..entrenamiento.models import UserProfile
from .forms import RegisterForm


# Create your views here.

@login_required
def inicio(request):
    try:
        perfil = UserProfile.objects.get(user=request.user)

        return render(
            request,
            'base.html',
            context={'perfil': perfil}
        )
    except UserProfile.DoesNotExist:
        perfil = UserProfile.objects.create(user=request.user)
    return render(
        request,
        'base.html'
    )


@login_required
def perfil(request):
    user = UserProfile(request)
    if not user:
        return redirect('edit_perfil')

    return render(
        request,
        'perfil.html'
    )


def contacto(request):

    return render(
        request,
        'contacto.html'
    )


def registro(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                return render(
                    request,
                    'registration/registro.html',
                    context={
                        'form': form,
                        'error': 'Correo electrónico ya registrado, intenta con otro. GAF@'}
                )

            user = form.save()
            login(request, user)

            profile_exists = UserProfile.objects.filter(
                user=request.user).exists()
            if not profile_exists:
                UserProfile.objects.create(user=request.user)
            return redirect('perfil')

    else:
        form = RegisterForm()

    return render(
        request,
        'registration/registro.html',
        context={'form': form})


def acceder(request):

    return render(
        request,
        './registration/login.html'
    )


def salir(request):
    logout(request)

    return redirect('inicio')