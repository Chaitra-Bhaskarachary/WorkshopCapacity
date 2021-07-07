from django.shortcuts import render, redirect
from .forms import WorkshopCapacityForm

# Create your views here.
# relative import of forms
from .models import WorkshopCapacity
from .forms import WorkshopCapacityForm

def entry_list(request):
    return render(request,"capacity/entry_list.html")

def entry_form(request):
    if request.method=="GET":
        form = WorkshopCapacityForm()
        return render(request,"capacity/entry_form.html", {'form':form})
    else:
        form = WorkshopCapacityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('entry/list')

def entry_delete(request):
    return