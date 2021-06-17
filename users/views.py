from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm # el nombre es bastante descriptivo jeje fijarse que es de forms


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # se muestra un form en blanco para registrarlo
        form = UserCreationForm()
    else:
        # se procesa un form completado
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()  # guardo un objeto 'user' en la variablo new_user que dsp se pasa como parametro a login()
            # logear al usuario y redirigirlo a la pagina de inicio
            login(request, new_user)  # funcion propia de django, fabulosa
            return redirect('learning_logs:index')
    # se muestra un form vacio o invalido
    context = {'form': form}
    return render(request, 'registration/register.html', context)
