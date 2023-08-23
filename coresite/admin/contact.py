from django.contrib import admin
from coresite.models.contact import Contact

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ('id', 'name', 'message', 'email', 'telephone')