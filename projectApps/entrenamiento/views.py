import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
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


def rutinas(request):
    rutinas = Routine.objects.all()

    return render(
        request,
        'rutinas/rutinas.html',
        context={'rutinas': rutinas})


class Rutinas(View):
    # con esta funcion se mostrara una vita que cargue las rutinas
    def get(self, request):
        rutinasHechas = list(Routine.objects.values())
        if len(rutinasHechas) > 0:
            datos = {'mensaje': 'aqui está la data', 'rutinas': rutinasHechas}

        else:
            datos = {'mensaje': 'la data no existe'}

        return render(
            request,
            'rutinas/rutinas.html',
            context={'datos': datos}
        )
    # con esta vista se mostrará una rutina seleccionada en la vista anterior

    def aggRut(self, request):
        datos = {'mensaje': 'rutina creada con exito'}
        jd = json.loads(request.body)

        if 'rutinas' in jd:
            form = RoutinesForm(request.POST)
            form.save()
            id = form.instance.id
            return redirect(reverse('addRutExer', kwargs={'id': id}))
        else:
            datos = {'mensaje': 'no se encontraron datos'}
            form = RoutinesForm()

        return render(
            request,
            'rutinas/crearRutina.html',
            context={'datos': datos, 'form': form})

    def put(self, request):
        pass

    def delete(self, request):
        pass


def getRut(request, id):

    rutinas = RoutineExercise.objects.all()
    rutina = rutinas.filter(routine_id=id)

    if len(rutina) > 0:
        datos = {'mensaje': 'aqui está la data', 'rutina': rutina}

    else:
        datos = {'mensaje': 'la rutina está vacía'}

    return render(
        request,
        'rutinas/rutina.html',
        context={'datos': datos}
    )


class Ejercicios(View):
    """ def aggExercises(self, request):

        datos = {'mensaje': 'rutina creada con exito'}
        jd = json.loads(request.body)

        if 'rutinas' in jd:
            rutinas_data = jd['rutinas']
            for element in rutinas_data:
                RoutineExercise.objects.create(
                    routine_id=element['routine_id'],
                    exercise_id=element['exercise_id'],
                    repetitions=element['repetitions'],
                    sets=element['sets']
                )
        else:
            datos = {
                'mensaje': 'La clave "rutinas" no está presente en los datos JSON'}

        return JsonResponse(datos) """
    pass


def aggRut(request):
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
