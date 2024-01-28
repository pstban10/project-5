from django.contrib import admin
from django.contrib.auth import urls as cuentas
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('projectApps.navbar.urls')),
    path('bh/', include('projectApps.entrenamiento.urls')),
    path('cls/', include('projectApps.clases.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include(cuentas)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
