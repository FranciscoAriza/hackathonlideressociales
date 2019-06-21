from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def index(request):
    user = request.user
    messages_pendientes = []
    lider_acreditado = Lider.objects.filter(usuario=user.id)
    if len(lider_acreditado) <= 0:
        messages_pendientes.append(
            "Recuerda que el cuídado de la vida inicia con la autoprotección.")
    context = {
        'messages_pendientes': messages_pendientes
    }
    return render(request, 'lideres/index.html', context)


def autoproteccion(request):
    return render(request, 'lideres/autoproteccion.html')


def about(request):
    return render(request, 'lideres/about.html')


def perfil(request):
    user = request.user
    messages = []

    if request.method == 'GET':
        lider_acreditado = Lider.objects.filter(usuario=user.id)
        if len(lider_acreditado) == 1:
            post = get_object_or_404(Lider, usuario=user.id)
            Formulario_form = AcreditarLiderForm(instance=post)
        else:
            Formulario_form = AcreditarLiderForm()
    elif request.method == 'POST':
        Formulario_form = AcreditarLiderForm(request.POST)
        if Formulario_form.is_valid():
            Formulario_form.save()
            state = 'ok'
            messages.append('Los datos del perfil se han actualizado exitosamente.')
        else:
            state = 'error'
            messages.append('Por favor revise la información ingresada')
    else:
        Formulario_form = AcreditarLiderForm()

    context = {
        'messages': messages,
        'form': Formulario_form
    }
    return render(request, 'lideres/perfil.html', context)


def denuncia(request):
    user = request.user
    messages = []

    if request.method == 'GET':
        Formulario_form = DenunciaLiderForm()
    elif request.method == 'POST':
        Formulario_form = DenunciaLiderForm(request.POST)
        if Formulario_form.is_valid():
            Formulario_form.save()
            state = 'ok'
            messages.append('La denuncia se registro exitosamente.')
        else:
            state = 'error'
            messages.append('Por favor revise la información ingresada')
    else:
        Formulario_form = DenunciaLiderForm()

    context = {
        'messages': messages,
        'form': Formulario_form
    }
    return render(request, 'lideres/denuncia.html', context)