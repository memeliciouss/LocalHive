from django.shortcuts import render, redirect 
from create.models import Events

# Create your views here.
def create(request):
    if request.method == 'POST':
        eventName = request.POST.get('eventName')
        sport = request.POST.get('sport')
        location = request.POST.get('location')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        event = Events(eventName=eventName, sport=sport, location=location, desc=desc, date=date)
        event.save()
        return redirect('home.index')
    return render(request, 'create.html')