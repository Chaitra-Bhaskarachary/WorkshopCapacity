from django.shortcuts import render, redirect
from .forms import WorkshopCapacityForm
from .models import WorkshopCapacity


def entry_list(request):
    context ={'entry_list': WorkshopCapacity.objects.all()}
    return render(request,"capacity/entry_list.html", context)

def entry_form(request, id=0):
    if request.method=="GET":
        if id==0:
            form = WorkshopCapacityForm()
        else:
            entry = WorkshopCapacity.objects.get(pk=id)
            form = WorkshopCapacityForm(instance=entry)
        return render(request,"capacity/entry_form.html", {'form':form})
    else:
        if id == 0:
            form = WorkshopCapacityForm(request.POST)
        else:
            entry = WorkshopCapacity.objects.get(pk=id)
            form = WorkshopCapacityForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
        return redirect('/entry/list')

def entry_delete(request, id):
    entry = WorkshopCapacity.objects.get(pk=id)
    entry.delete()
    return redirect('/entry/list')