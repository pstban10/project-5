from django.contrib import admin
from django.contrib.auth import urls as cuentas
from django.urls import path, include

urlpatterns = [
    path('', include('navbar.urls')),
    path('bh/', include('entrenamiento.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include(cuentas)),

]
