import json
from urllib.parse import parse_qs
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .forms import ExerciseForm, ProfileForm, RoutineExerciseForm, UserRoutinesForm, RoutinesForm
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


class RutinasList(ListView):
    model = Routine
    template_name = 'rutinas/rutinas.html'


class RutinasCreator(CreateView):
    model = Routine
    form_class = RoutinesForm
    template_name = 'rutinas/crearRutina.html'
    success_url = reverse_lazy('rutina:RutinasEditor')


class RutinaEditor(ListView):
    model = Exercise
    form_class = RoutineExerciseForm
    template_name = 'rutinas/addRutExe.html'
    success_url = reverse_lazy('rutina:RutinasList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rutina'] = Routine.objects.get(id=self.kwargs['id'])
        return context


def newRut(request):
    if request.method == 'POST':
        form = RoutinesForm(request.POST)
        form.save()
        RutId = Routine.objects.last().id
        return redirect('RutinaEditor', id=RutId)
    else:
        return redirect('RutinasCreator')


def putRut(request):

    if request.method == 'POST':

        print('hola')

    """ if 'rutinas' in jd:
        form = RoutinesForm(request.POST)
        form.save()
        id = form.instance.id
        return redirect(reverse('addRutExer', kwargs={'id': id}))
    else:
        datos = {'mensaje': 'no se encontraron datos'}
        form = RoutinesForm() """

    """ for element in data['rutinas']:
        RoutineExercise.objects.create(
            routine_id=element['routine_id'],
            exercise_id=element['exercise_id'],
            repetitions=element['repetitions'],
            sets=element['sets']
        ) """

    return redirect('RutinasList')
