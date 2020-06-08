from django.shortcuts import render, HttpResponse

# Create your views here.
def servicios(request): 
    return render(request, "core2/servicios.html") 
def contacto(request): 
    return render(request, "core2/contacto.html") 
def portada(request): 
    return render(request, "core2/portada.html") 
def perfil(request): 
    return render(request, "core2/perfil.html") 
   