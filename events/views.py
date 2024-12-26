from django.shortcuts import render, redirect
from events.models import Events

# Create your views here.
def index(request):
    events=Events.objects.all()

    return render(request, 'index.html', {'events':events})


def create(request):
    if request.method == 'POST':
        eventName = request.POST.get('eventName')
        sport = request.POST.get('sport')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        location = request.POST.get('location')
        event=Events(eventName=eventName, sport=sport, desc=desc, date=date, location=location)
        event.save()
        return redirect('/')

    return render(request, 'create.html')