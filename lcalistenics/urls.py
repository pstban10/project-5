from django.contrib import admin
from django.contrib.auth import urls as cuentas
from django.urls import path, include

urlpatterns = [
    path('', include('projectApps.navbar.urls')),
    path('bh/', include('projectApps.entrenamiento.urls')),
    path('agd/', include('projectApps.agenda.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include(cuentas)),

]
