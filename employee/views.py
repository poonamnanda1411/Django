from django.shortcuts import render
from .models import Person
from .forms import empForm
from django.http import HttpResponse

# Create your views here.
def create_view(request):
    context={}
    
    form=empForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('Person has been added!')
    context['form']=form

    return render(request,"employees/create_view.html",context)
    