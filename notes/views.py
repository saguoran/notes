from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required # Add this
from django.http import HttpResponseForbidden

# Updated List View
@login_required
def note_list(request):
    query = request.GET.get('q')
    if query:
        # Search in both title and content
        notes = Note.objects.filter(
            user=request.user,
            title__icontains=query
        ) | Note.objects.filter(
            user=request.user,
            content__icontains=query
        )
    else:
        notes = Note.objects.filter(user=request.user)
    
    notes = notes.order_by('-updated_at')
    return render(request, 'notes/note_list.html', {'notes': notes})

# New Create View
@login_required
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

@login_required
def note_update(request, pk):
    # pk is the "Primary Key" (the UUID) of the note
    note = get_object_or_404(Note, pk=pk)
    
    # Security: Ensure this note belongs to the logged-in user
    if note.user != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    
    if note.user != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        note.delete()
        return redirect('note_list')
        
    return render(request, 'notes/note_confirm_delete.html', {'note': note})