from django.shortcuts import render , get_object_or_404
from Noticias.models import Noticia

# Create your views herec

def noticia_detalle(request, Noticia_id):
    noticia= get_object_or_404(Noticia, id=Noticia_id)
    return render(request, 'noticia_codigo.html', {'noticia': noticia})
