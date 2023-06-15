from django.shortcuts import render
from .models import Person 

# Create your views here.
def homeView(request):
    personlist = Person.objects.all()
    context = {
        'persons':personlist
    }
    return render(request, 'person/index.html', context)

def tableView(request):
    context = {}
    return render(request, 'person/table.html', context)