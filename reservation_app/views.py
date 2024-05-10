from django.shortcuts import render, redirect
from .forms import SalaForm, ModifySalaForm, ReserveSalaForm
from .models import Sala, Rezerwacja
from datetime import date
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


def add_room(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            nazwa_sali = form.cleaned_data['name']
            pojemnosc_sali = form.cleaned_data['capacity']
            rzutnik_dostepnosc = form.cleaned_data['projector_availability']

            if Sala.objects.filter(name=nazwa_sali).exists():
                return render(request, 'add_room.html',
                              {'form': form, 'error_message': 'Sala o tej nazwie już istnieje'})

            if pojemnosc_sali <= 0:
                return render(request, 'add_room.html',
                              {'form': form, 'error_message': 'Pojemność sali musi być liczbą dodatnią'})

            sala = Sala(name=nazwa_sali, capacity=pojemnosc_sali, projector_availability=rzutnik_dostepnosc)
            sala.save()
            return redirect('lista_sal')

    else:
        form = SalaForm()
    return render(request, 'add_room.html', {'form': form})


def lista_sal(request):
    sale = Sala.objects.all()
    dzis = date.today()
    return render(request, 'lista_sal.html', {'sale': sale, 'dzis': dzis})


def delete_room(request, id):
    sala = Sala.objects.get(pk=id)
    sala.delete()
    return redirect('lista_sal')


def modify_room(request, id):
    sala = Sala.objects.get(pk=id)

    if request.method == 'POST':
        form = ModifySalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('lista_sal')
    else:
        form = ModifySalaForm(instance=sala)

    return render(request, 'modify_room.html', {'form': form})


def reserve_room(request, id):
    sala = Sala.objects.get(pk=id)

    if request.method == 'POST':
        form = ReserveSalaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            komentarz = form.cleaned_data['komentarz']

            if Rezerwacja.objects.filter(sala=sala, data=data).exists():
                form.add_error(None, "Sala jest już zarezerwowana w wybranej dacie.")
            elif data < date.today():
                form.add_error('data', "Nie można zarezerwować sali w przeszłości.")
            else:
                Rezerwacja.objects.create(sala=sala, data=data, komentarz=komentarz)
                return redirect('lista_sal')
    else:
        form = ReserveSalaForm()

    return render(request, 'reserve_room.html', {'form': form})


def sala_detail(request, id):
    sala = Sala.objects.get(pk=id)
    rezerwacje = Rezerwacja.objects.filter(sala=sala).order_by('data')
    dzis = date.today()

    if request.method == 'POST':
        form = ReserveSalaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            komentarz = form.cleaned_data['komentarz']
            if Rezerwacja.objects.filter(sala=sala, data=data).exists():
                form.add_error(None, "Sala jest już zarezerwowana w wybranej dacie.")
            elif data < dzis:
                form.add_error('data', "Nie można zarezerwować sali w przeszłości.")
            else:
                Rezerwacja.objects.create(sala=sala, data=data, komentarz=komentarz)
                return redirect('sala_detail', id=id)
    else:
        form = ReserveSalaForm()

    return render(request, 'sala_detail.html', {'sala': sala, 'rezerwacje': rezerwacje, 'form': form})
