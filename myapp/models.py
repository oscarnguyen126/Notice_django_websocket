from django.db import models
from .consumers import NotificationConsumer

class Notification(models.Model):
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.message


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)