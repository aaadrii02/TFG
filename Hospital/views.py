from django.shortcuts import render, redirect
from Hospital.forms import *
from Hospital.models import *
from django.http import JsonResponse

# Create your views here.

def login(request):
    if request.method=='POST':
        my_form=FrmLogin(request.POST)
        if my_form.is_valid():
            usuario=buscar_medico(request)
            if usuario!=None:
                request.session["dni"] = usuario.dni
                request.session["nombre"] = usuario.nombre
                return render(request,'medico.html',{'u':usuario, "dni":request.session["dni"], "nombre":request.session["nombre"]})
            else:
                usuario=buscar_paciente(request)
                if usuario!=None:
                    request.session["dni"] = usuario.dni
                    request.session["nombre"] = usuario.nombre
                    ficha=buscar_ficha(request.session['dni'])
                    return render(request, 'paciente.html',{'u':ficha, "dni":request.session["dni"], "nombre":request.session["nombre"]})
                else:
                    usuario=buscar_admin(request)
                    if usuario!=None:
                        request.session["dni"] = usuario.dni
                        request.session["nombre"] = usuario.nombre
                        return render(request, 'admin.html',{'u':usuario, "dni":request.session["dni"], "nombre":request.session["nombre"]})
                    else: 
                        my_form=FrmLogin()
                        return render(request,'login.html',{'form':my_form, "error": "Credenciales incorrectas"})
    else:
        my_form=FrmLogin()
        return render(request, 'login.html', {'form':my_form})
    
def buscar_paciente(request):
    my_form=FrmLogin(request.POST)
    if my_form.is_valid():
        try:
            usuario=paciente.objects.get(usuario=my_form.cleaned_data['usuario'])
        except paciente.DoesNotExist:
            return None
        else:
            return usuario
        
def buscar_medico(request):
    my_form=FrmLogin(request.POST)
    if my_form.is_valid():
        try:
            usuario=medico.objects.get(usuario=my_form.cleaned_data['usuario'])
        except medico.DoesNotExist:
            return None
        else:
            return usuario
        

def verPacientes(request):
    lista_info=list(paciente.objects.all())
    return render(request,'verPacientes.html',{'lista':lista_info})

def buscar_por_dni(request):
    if request.method == 'GET':
        dni = request.GET.get('dni')
        if dni:
            pacientes = paciente.objects.filter(dni=dni)
        else:
            pacientes = paciente.objects.none()
        return render(request, 'verPacientes.html', {'pacientes': pacientes})
    
    
def buscar_ficha_paciente(request, dni):
    ficha=ficha_medica.objects.filter(dni_paciente=dni)
    return render(request, 'ficha.html', {'o':ficha})

def verCitas(request):
    citas=cita.objects.all().filter(dni_medico=request.session["dni"])
    return render(request, 'verCitas.html', {'c':citas})

def modificarFicha(request):
    if request.method == 'POST':
        form = FrmModificarFicha(request.POST)
        if form.is_valid():
            observaciones = form.cleaned_data['observaciones']

            # Obtener el objeto existente o crear uno nuevo si no existe
            objeto = ficha_medica.objects.first()
            if objeto is None:
                objeto = ficha_medica()

            # Concatenar el nuevo string al campo existente
            objeto.observaciones = objeto.observaciones +". "+observaciones
            objeto.save()

            return render(request, 'modificarFicha.html', {'mensaje':'Observaciones guardadas con éxito', 'form':FrmModificarFicha()})  # Redirigir a otra vista después de guardar
    else:
        form = FrmModificarFicha()

    return render(request, 'modificarFicha.html', {'form': form})

    

#ANGEL

def buscar_ficha(dni):
    try:
        ficha=ficha_medica.objects.get(dni_paciente=dni)
    except ficha_medica.DoesNotExist:
        return None
    else:
        return ficha

def pedirCita(request):
    if request.method=='POST':
        my_frm=FrmCita(request.POST)
        if my_frm.is_valid():
            dicc = my_frm.cleaned_data
            c = cita(especialidad=dicc['especialidad'], dni_paciente=request.session["dni"], nombre_medico=dicc['nombre_medico'], fecha_hora=dicc['fecha_hora'], dni_medico=dicc['dni_medico'])
            c.save()
            return render(request, 'pedirCita.html', {'mensaje':'Cita registrada con éxito', 'form':FrmCita()})
    my_frm=FrmCita()
    my_frm.fields['dni_paciente'].initial=request.session["dni"]
    my_frm.fields['dni_paciente'].widget.attrs['readonly']=True
    return render(request, 'pedirCita.html',{'form':my_frm})

def gestionarCita(request):
    citas=cita.objects.all().filter(dni_paciente=request.session["dni"])   
    return render(request, 'gestionarCita.html',{'citas':citas})

def borrar(request,val):
    c=cita.objects.get(id=val).delete()
    return redirect('gestionarCita')

def editar(request,val):
    c=cita.objects.get(id=val)
    if request.method=='POST':
        my_frm=FrmCita(request.POST)
        if my_frm.is_valid():
            c.fecha_hora=my_frm.cleaned_data['fecha_hora']
            c.save()
            return redirect('gestionarCita')
    my_frm=FrmCita()
    my_frm.fields['especialidad'].initial=c.especialidad
    my_frm.fields['dni_paciente'].initial=c.dni_paciente
    my_frm.fields['nombre_medico'].initial=c.nombre_medico
    my_frm.fields['fecha_hora'].initial=c.fecha_hora
    my_frm.fields['dni_medico'].initial=c.dni_medico
    my_frm.fields['especialidad'].widget.attrs['readonly']=True
    my_frm.fields['dni_paciente'].widget.attrs['readonly']=True
    my_frm.fields['nombre_medico'].widget.attrs['readonly']=True
    my_frm.fields['dni_medico'].widget.attrs['readonly']=True
    return render(request, 'pedirCita.html', {'form':my_frm})

def buscar_admin(request):
    my_form=FrmLogin(request.POST)
    if my_form.is_valid():
        try:
            usuario=administrador.objects.get(usuario=my_form.cleaned_data['usuario'])
        except administrador.DoesNotExist:
            return None
        else:
            return usuario
        
def verMedicos(request):
    lista_info=list(medico.objects.all())
    return render(request,'verMedicos.html',{'lista':lista_info})

def borrarMedico(request,val):
    m=medico.objects.get(dni=val).delete()
    return redirect('verMedicos')

def altaMedico(request):
    if request.method=='POST':
        my_frm=FrmMedico(request.POST)
        if my_frm.is_valid():
            dicc = my_frm.cleaned_data
            m = medico(especialidad=dicc['especialidad'], dni=dicc["dni"], nombre=dicc['nombre'], usuario=dicc['usuario'], password=dicc['password'])
            m.save()
            return render(request, 'alta.html', {'mensaje':'Medico dado de alta con éxito', 'form':FrmMedico()})
    my_frm=FrmMedico()
    return render(request, 'alta.html',{'form':my_frm})

def borrarPaciente(request,val):
    p=paciente.objects.get(dni=val).delete()
    return redirect('verPacientesAdmin')

def altaPaciente(request):
    if request.method=='POST':
        my_frm=FrmPaciente(request.POST)
        if my_frm.is_valid():
            dicc = my_frm.cleaned_data
            p = paciente(dni=dicc["dni"], nombre=dicc['nombre'], usuario=dicc['usuario'], password=dicc['password'])
            p.save()
            return render(request, 'alta.html', {'mensaje':'Paciente registrado con éxito', 'form':FrmPaciente()})
    my_frm=FrmPaciente()
    return render(request, 'alta.html',{'form':my_frm})

def verPacientesAdmin(request):
    lista_info=list(paciente.objects.all())
    return render(request,'verPacientesAdmin.html',{'lista':lista_info})


##### VOLVER A TRAS #####

def pacienteBack(request):
    ficha=buscar_ficha(request.session['dni'])
    return render(request, 'paciente.html',{'u':ficha, "dni":request.session["dni"], "nombre":request.session["nombre"]})

                
