from django.contrib import admin
from coresite.models.policy import Policy

@admin.register(Policy)
class AdminPolicy(admin.ModelAdmin):
    list_display = ('id', 'title')