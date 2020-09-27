from django.conf.urls import include, url
from . import views
from django.urls import path


urlpatterns = [
     url(r'^$', views.inicio, name="paginaprincipal"),
     url('trabajadores/inicio', views.redirigir, name="redirigir"),
     url('trabajadores/login', views.login , name="login"),
      path('agregarclientes',views.agregarclientes, name="adm.inicio" ),
      path('crearficha',views.crearficha, name="orden"),
     url('trabajadores/clientes', views.verClientes, name="clientes"),
     url('trabajadores/clientesadm', views.verClientesAdmin, name="clientes.adm"),
     url('trabajadores/fichas', views.verFichas, name="fichas"),
     url('trabajadores/fichasadm', views.verFichasAdmin, name="fichas.adm"),
]
