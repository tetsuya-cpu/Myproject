from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.db.models import Q

def person_list(request):
    query = request.GET.get('q')
    if query:
        people = Person.objects.filter(
            Q(name__icontains=query) |
            Q(age__icontains=query) |
            Q(birthdate__icontains=query) |
            Q(description__icontains=query) |
            Q(salary__icontains=query)
        )
    else:
        people = Person.objects.all()
    return render(request, 'records/person_list.html', {'people': people})

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'records/person_form.html', {'form': form})

def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'records/person_form.html', {'form': form})

def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'records/person_confirm_delete.html', {'person': person})