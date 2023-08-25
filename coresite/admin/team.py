from django.contrib import admin
from coresite.models.team import Team

@admin.register(Team)
class AdminTeam(admin.ModelAdmin):
    list_display = ('id', 'title')