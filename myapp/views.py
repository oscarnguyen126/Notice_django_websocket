from django.shortcuts import render
from .models import Note, Notification


# Create your views here.
def index(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = Note(title=title, content=content)
        note.save()
        return render(request, 'index.html', {'note': note})
    
    return render(request, 'create.html')
