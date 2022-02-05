from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'index.html')


def produtos(request):
    return render(request, 'produtos.html')


def contato(request):
    if request.method == 'POST':
        messages.success(request, 'Este site é apenas para Portfolio. Nenhum dado será armazenado. Obrigada por visualizar nosso site!')
        return redirect('contato')
    return render(request, 'contato.html')