from django.urls  import path
from . import views
urlpatterns = [
    path("",views.inicio, name = "InicioPag"),
    path("buscar/<comision>", views.buscar_comision, name = "BuscarHilo"),
    path("buscar/resultados",views.inicio, name = "InicioPag"),
]