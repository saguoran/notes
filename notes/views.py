from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm

# Updated List View
def note_list(request):
    notes = Note.objects.all().order_by('-updated_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

# New Create View
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            # For now, we manually assign the first user (you) 
            # until we set up the Login system next.
            from django.contrib.auth.models import User
            note.user = User.objects.first() 
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})