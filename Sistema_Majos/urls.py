"""
URL configuration for Sistema_Majos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("login.urls")),
    path('home_sistema/', include("sistema_home.urls")),
    path('parametros/', include("parametros.urls")),
    path('nevera/', include("nevera.urls")),
    path('freidora/', include("freidora.urls")),
    path('limpieza/', include("limpieza.urls")),
    path('edit_parametros/', include("edit_parametros.urls")),
    path('historial/', include("historial.urls")),
]
