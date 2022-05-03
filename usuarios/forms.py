from django.forms import forms 

class FormProfesor(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    email = forms.EmailField()
    web = forms.CharField(max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)
    comision = forms.IntegerField()
