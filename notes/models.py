import uuid
from django.db import models
from django.contrib.auth.models import User # This is Django's built-in User system

class Note(models.Model):
    # We use UUID instead of a simple 1, 2, 3 ID. 
    # This is better for syncing between different devices.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # This links the note to a specific user.
    # If the user is deleted, their notes are deleted too (on_delete=models.CASCADE).
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    
    # These track when you created and last edited the note.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title if self.title else "Untitled Note"