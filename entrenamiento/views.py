from django.shortcuts import redirect, render
from .forms import ExerciseForm, ProfileForm
from .models import Exercise, UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def perfil(request):
    perfil = UserProfile.objects.get(user=request.user)
    return render(
        request,
        'profile.html',
        context={'perfil': perfil})


@login_required
def edit_perfil(request):
    perfil = UserProfile.objects.get(user=request.user)
    form = ProfileForm(instance=perfil)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('perfil')

    return render(
        request,
        'edit_profile.html',
        context={'form': form})


def aggejercicio(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        form.save()
        return redirect('ejercicios')
    else:
        form = ExerciseForm()

    return render(
        request,
        'aggejercicio.html',
        context={'form': form})


def rutinas(request):
    return render(
        request,
        'rutinas.html')


def ejercicios(request):
    ejercicios = Exercise.objects.all()

    return render(
        request,
        'exercises.html',
        context={'ejercicios': ejercicios})
