from django import forms
# Importamos el Modelo de Peros_Rescatados
from .models import RegistroCliente, OrdenTrabajo
from django.conf import settings


# Crear el formulario de Perro Rescatad


class RegistroCliente_form(forms.ModelForm):
	class Meta:
		model = RegistroCliente
		fields = ('Nombre_Completo', 'Direccion', 'Ciudad', 'Comuna', 'Correo','Tecnico_Asociado' )

class OrdenTrabajo_form(forms.ModelForm):
	class Meta:
		model = OrdenTrabajo
		fields = [  
                    'Folio',
                    'Cliente',
                    'fecha',
                    'hora_inicio',
                    'hora_termino',
                    'Id_ascensor',
                    'modelo_ascensor',
                    'fallas',
                    'piezas_cambiadas',
                    'Nombre_Tecnico']


widgets = {
                'fecha': forms.DateInput(attrs={'class': 'datepicker'}),
}
