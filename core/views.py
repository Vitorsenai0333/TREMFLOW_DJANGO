from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


@login_required
def pedidos(request):
    return render(request, 'pedidos.html')