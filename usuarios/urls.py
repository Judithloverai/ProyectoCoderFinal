from django.urls  import path
from . import views
urlpatterns = [
    path("",views.inicio, name = "Inicio"),
    path("nuevo_profesor",views.nuevo_profesor, name = "NuevoProfesor"),

]