"""HospitalAcuario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login, name="login"),
    path('verPacientes', verPacientes, name="verPacientes"),
    path('buscar_por_dni', buscar_por_dni, name='buscar_por_dni'),
    path('buscar_ficha_paciente/<str:dni>',buscar_ficha_paciente, name="buscar_ficha_paciente"),
    path('pedirCita', pedirCita, name="pedirCita"),
    path('gestionarCita', gestionarCita, name="gestionarCita"),
    path('borrar/<str:val>', borrar, name='borrar'),
    path('editar/<str:val>', editar, name='editar'),
    path('verCitas',verCitas, name="verCitas"),
    path('modificarFicha', modificarFicha, name='modificarFicha'),
    path('verMedicos', verMedicos, name="verMedicos"),
    path('borrarMedico/<str:val>', borrarMedico, name='borrarMedico'),
    path('altaMedico', altaMedico, name="altaMedico"),
    path('borrarPaciente/<str:val>', borrarPaciente, name='borrarPaciente'),
    path('altaPaciente', altaPaciente, name="altaPaciente"),
    path('verPacientesAdmin', verPacientesAdmin, name="verPacientesAdmin"),
    path('pacienteBack', pacienteBack, name="pacienteBack"),
    path('modificarFicha', modificarFicha, name='modificarFicha'),
    
    
    
]

