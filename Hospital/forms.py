from django import forms

class FrmLogin(forms.Form):
    usuario=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Usuario"}),label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput({'class':'form-control','placeholder':"Escribe tu contraseña"}), label="Contraseña", min_length=3)
    
class FrmCita(forms.Form):
    especialidad=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Especialidad"}),label="Especialidad")
    dni_paciente=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"DNI"}),label="DNI")
    nombre_medico=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Medico"}),label="Medico") #SACARLOS POR ESPECIALIDAD
    fecha_hora=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Fecha y hora"}),label="Fecha y hora") #MODIFICAR CUANDO LA FECHA FUNCIONE
    dni_medico=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"DNI"}),label="DNI MEDICO")
    
class FrmMedico(forms.Form):
    especialidad=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Especialidad"}),label="Especialidad")
    dni=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"DNI"}),label="DNI")
    nombre=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Medico"}),label="Nombre")
    usuario=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Usuario"}),label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput({'class':'form-control','placeholder':"Escribe tu contraseña"}), label="Contraseña", min_length=3)
    
class FrmPaciente(forms.Form):
    dni=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"DNI"}),label="DNI")
    nombre=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Paciente"}),label="Nombre")
    usuario=forms.CharField(widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Usuario"}),label="Usuario")
    password=forms.CharField(widget=forms.PasswordInput({'class':'form-control','placeholder':"Escribe tu contraseña"}), label="Contraseña", min_length=3)
    
class FrmModificarFicha(forms.Form):
    observaciones = forms.CharField(max_length=200)