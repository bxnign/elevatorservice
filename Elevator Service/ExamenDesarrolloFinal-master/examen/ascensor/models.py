from django.db import models
from django.utils import timezone

#Permisos DJANGO 
from django.utils.translation import ugettext as _


class OrdenTrabajo (models.Model):
    Folio = models.CharField(primary_key=True, max_length=5)
    Cliente = models.CharField(max_length=40, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_termino = models.TimeField(blank=True, null=True)
    Id_ascensor =  models.CharField(max_length=40,blank=True, null=True)
    modelo_ascensor = models.CharField(max_length=200, blank=True, null=True)
    fallas = models.TextField()
    piezas_cambiadas = models.TextField()
    Nombre_Tecnico = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def _str_(self):
        return self.Folio


    def __str__(self):
        return '{}'.format(self.Nombre_Tecnico)

class RegistroCliente (models.Model):
    Nombre_Completo = models.CharField(max_length=200, blank=True, null=True)
    Direccion = models.CharField(max_length=200, blank=True, null=True)
    Ciudad = models.CharField(max_length=200, blank=True, null=True)
    Comuna = models.CharField(max_length=200, blank=True, null=True)
    Correo = models.EmailField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    Tecnico_Asociado = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
  

    def _str_(self):
        return self.Nombre_Completo

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return '{}'.format(self.Tecnico_Asociado)

