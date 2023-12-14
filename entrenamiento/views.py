from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import ExerciseForm, ProfileForm, UserRoutinesForm, RoutinesForm
from .models import Exercise, UserProfile, UserRoutine, Routine, RoutineExercise
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def perfil(request):
    perfil = UserProfile.objects.get(user=request.user)
    return render(
        request,
        'perfil/profile.html',
        context={'perfil': perfil})


@login_required
def edit_perfil(request):
    perfil = UserProfile.objects.get(user=request.user)
    form = ProfileForm(instance=perfil)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')

    return render(
        request,
        'perfil/edit_profile.html',
        context={'form': form})


def ejercicios(request):
    ejercicios = Exercise.objects.all()

    return render(
        request,
        'ejercicios/exercises.html',
        context={'ejercicios': ejercicios})


def aggejercicio(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        form.save()
        return redirect('ejercicios')
    else:
        form = ExerciseForm()

    return render(
        request,
        'ejercicios/aggejercicio.html',
        context={'form': form})


def rutinas(request):
    rutinas = Routine.objects.all()

    return render(
        request,
        'rutinas/rutinas.html',
        context={'rutinas': rutinas})


def aggRutina(request):
    if request.method == 'POST':
        form = RoutinesForm(request.POST)
        form.save()
        id = form.instance.id
        return redirect(reverse('addRutExer', kwargs={'id': id}))
    else:
        form = RoutinesForm()

    return render(
        request,
        'rutinas/crearRutina.html',
        context={'form': form})


def aggRutExer(request, id):
    rutina = Routine.objects.get(id=id)
    ejercicios = Exercise.objects.all()
    return render(
        request,
        'rutinas/addRutExe.html',
        context={'rutina': rutina, 'ejercicios': ejercicios}
    )


def rutina(request, id):
    rutina = Routine.objects.get(id=id)
    return render(
        request,
        'rutinas/rutina.html',
        context={'rutina': rutina})


def agenda(request):

    return render(
        request,
        'agenda.html',

    )


def addAgenda(request):
    pass
