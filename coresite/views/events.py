from typing import Any
from django.db.models.query import QuerySet
from django.views import generic

from coresite.models import Event

class EventsView(generic.ListView):
    '''
    ListView used for our Events page

    Template:
    :template: `coresite/events.html`
    '''

    model = Event
    template_name = "core/events.html"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.active().order_by("-creation_date")
    