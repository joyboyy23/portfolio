from django.contrib import admin
from .models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
