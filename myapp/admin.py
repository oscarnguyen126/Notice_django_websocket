from django.contrib import admin
# 👇 1. Add this line import notification model
from .models import Notification, Note

# 👇 2. Add this line to add the notification
admin.site.register(Notification)
admin.site.register(Note)