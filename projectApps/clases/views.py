from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from projectApps.entrenamiento.models import UserProfile
from .models import Location, AvailableHour
from .models import TestClass
from .forms import TestClassForm


@login_required
def testClass(request):
    perfil = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = TestClassForm(request.POST)
        form.is_valid()
        form.save()
        return redirect('inicio')

    form = TestClassForm()
    return render(
        request,
        'reservaciones/clase_prueba.html',
        context={'form': form, 'perfil': perfil}
    )


def calendar(request):
    return render(
        request,
        'reservaciones/clase_prueba.html',
    )


def get_locations(request):

    lugares = list(Location.objects.values())
    if (len(lugares) > 0):
        data = {"Mensaje": "Éxito", "puntos": lugares}
    else:
        data = {"Mensaje": "no hay nada bro"}
    return JsonResponse(data)


"""     return render(
        request,
        'reservaciones/clase_prueba.html',
        context={"datos": data, 'form': form}

    ) """


def get_hours(request, location_id, weekday_id):
    hours = list(AvailableHour.objects.filter(
        location_id=location_id, weekday_id=weekday_id).values())

    if (len(hours) > 0):
        data = {"Mensaje": "Exito", "horarios": hours}
    else:
        data = {"Mensaje": "no hay nada bro"}
    return JsonResponse(data)


"""     return render(
        request,
        'reservaciones/clase_prueba.html',
        context={"datos": data, 'form': form}

    ) """
