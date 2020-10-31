from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import PlaceForm, UpdatePlaceForm
from django.http import HttpResponse, HttpResponseRedirect, request

def home(request):
    return render(request, "main.html")

def place(request):
    places = Place.objects.all()
    context = {
        'places': places,
    }
    return render(request, 'place_list.html', context)


def place_create(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save()
        return redirect('place-list')
    # else:
    #     form = PlaceForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         new_item = form.save()
    #     else:
    #         validation = 'error'
    #         return render(request, 'place_create.html', {'validation': validation})
    #     return redirect('place-create')
    form = PlaceForm(request.FILES)
    return render(request, 'place_create.html', {'form': form})


def place_update(request):
    if request.method == 'POST' and 'id' in request.POST:
        request.POST._mutable = True
        item = get_object_or_404(Place, pk=request.POST.get('id'))
        form = UpdatePlaceForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save()
        else:
            validation = 'error'
            return render(request, 'place_update.html', {'validation': validation})
    elif 'id' in request.GET:
        item = get_object_or_404(Place, pk=request.GET.get('id'))
        form = PlaceForm(instance=item)
        return render(request, 'place_update.html', {'form': form})
    return HttpResponseRedirect("../")
