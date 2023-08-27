from django.db.models.query import QuerySet
from django.views import generic

from coresite.models import Team

class TeamView(generic.ListView):
    '''
    ListView used for our team page

    Template:
    :template: `coresite/team.html`
    '''

    model = Team
    template_name = "core/team.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-creation_date")
    