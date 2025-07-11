from django.shortcuts import render, redirect, get_object_or_404
from .models import Compagnie
from .forms import CompagnieForm
from django.shortcuts import get_object_or_404

def compagnie_affiche(request):
    compagnies = Compagnie.objects.all()
    return render(request, 'compagnie/affiche.html', {'compagnies': compagnies})

def compagnie_ajout(request):
    if request.method == 'POST':
        form = CompagnieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compagnie_affiche')
    else:
        form = CompagnieForm()
    return render(request, 'compagnie/ajout.html', {'form': form})

def compagnie_update(request, id):
    compagnie = get_object_or_404(Compagnie, pk=id)
    if request.method == 'POST':
        form = CompagnieForm(request.POST, instance=compagnie)
        if form.is_valid():
            form.save()
            return redirect('compagnie_affiche')
    else:
        form = CompagnieForm(instance=compagnie)
    return render(request, 'compagnie/update.html', {'form': form})

def compagnie_delete(request, id):
    compagnie = get_object_or_404(Compagnie, pk=id)
    if request.method == 'POST':
        compagnie.delete()
        return redirect('compagnie_affiche')
    return render(request, 'compagnie/delete.html', {'compagnie': compagnie})


def compagnie_detail(request, id):
    compagnie_obj = get_object_or_404(Compagnie, pk=id)
    return render(request, 'compagnie/detail.html', {'compagnie': compagnie_obj})
