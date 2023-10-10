from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    """faz um logout do usuario."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    """Faz o cadastro de um novo usuario."""
    if request.method != 'POST':
        # EXibi o formulario de cadastro em barnco
        form = UserCreationForm()

    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            new_user = form.save()
            # Faz login do usuário e o redirecioa parea a página inicial
            authenticated_user = authenticate(username= new_user.username, password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
