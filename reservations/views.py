from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm, UpdateReservationForm
from django.http import HttpResponse, HttpResponseRedirect, request

def reservation(request):
    reservations = Reservation.objects.all().order_by('-created_at')
    context = {
        'reservations': reservations,
    }
    return render(request, 'reservation_list.html', context)


def reservation_create(request):
    if request.method == 'POST':
        request.POST._mutable = True
        request.POST['user'] = request.user
        form = ReservationForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
        return redirect('reservation-list')
    form = ReservationForm(request.FILES)
    return render(request, 'reservation_create.html', {'form': form})


def reservation_update(request):
    if request.method == 'POST' and 'id' in request.POST:
        request.POST._mutable = True
        item = get_object_or_404(Reservation, pk=request.POST.get('id'))
        form = UpdateReservationForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
        else:
            validation = 'error'
            return render(request, 'reservation_update.html', {'validation': validation})
    elif 'id' in request.GET:
        item = get_object_or_404(Reservation, pk=request.GET.get('id'))
        form = ReservationForm(instance=item)
        return render(request, 'reservation_update.html', {'form': form})
    return HttpResponseRedirect("../")


def reservation_delete(request, id):
    item = get_object_or_404(Reservation, pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('reservation-list')  # 리스트 화면으로 이동합니다.
    return render(request, 'reservation_delete.html', {'item': item})