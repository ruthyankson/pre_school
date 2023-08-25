from django.contrib import admin
from coresite.models.event import Event

@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ('id', 'title')