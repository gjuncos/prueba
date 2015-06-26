from django.shortcuts import render
from  .forms import FormularioPagina
# Create your views here.
def mail(asunto,nombre,desde,para,cuerpo):
    print (asunto,nombre,desde,para,cuerpo)
    
def Contacto(request):
    consulta=None
    form=FormularioPagina()
    if request.method=="POST":
        form=FormularioPagina(request.POST)
        if form.is_valid():
            mail(*[form.cleaned_data[i] for i in ("asunto","nombre","mail","departamento","consulta")])
            return render (request, 'exito.html')
    return render(request, 'paginaContacto.html',{'form':form}) 
