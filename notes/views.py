from django.shortcuts import render
from .models import Note

def note_list(request):
    # This grabs all notes from the database
    notes = Note.objects.all().order_by('-updated_at')
    
    # This sends those notes to an HTML file (which we will create next)
    return render(request, 'notes/note_list.html', {'notes': notes})