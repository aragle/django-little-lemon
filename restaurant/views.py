# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)

# Add your code here to create new views


def menu(request):
    menu_items = Menu.objects.all()
    context = {'menu_items': menu_items}
    return render(request, 'menu.html', context)


def menu_detail(request, menu_id):
    menu_item = Menu.objects.get(id=menu_id)
    context = {'menu_item': menu_item}
    return render(request, 'menu_detail.html', context)
