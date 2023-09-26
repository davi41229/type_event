from django.shortcuts import render
from eventos.models import Certificado, Evento
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def meus_certificados(request):
    certificados = Certificado.objects.filter(participante=request.user)
    return render(request, 'meus_certificados.html', {'certificados': certificados})


def meus_eventos(request):
    nome =request.GET.get('nome')
    eventos = Evento.objects.filter(criador=request.user)
    if nome:
        eventos = eventos.filter(nome__contains=nome) #filter locaps

    return render(request, 'meus_eventos.html', {'eventos': eventos})
