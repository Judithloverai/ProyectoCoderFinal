from django.shortcuts import render

from usuarios.templates.usuarios.forms import FormProfesor
from .forms import FromProfesor

def inicio(request):
    return render(request, "usuarios/inicio.html")

def nuevo_profesor(request):
    if request.method == "POST":
        mi_form = FormProfesor()
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            profe = Profesor(nombre=info["nombre"])

    from = FromProfesores()
    return render(request, 'usuarios/formProfesores.html',{"form": mi_form})