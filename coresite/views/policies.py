from typing import Any
from django.db.models.query import QuerySet
from django.views import generic

from coresite.models import Policy

class PoliciesView(generic.ListView):
    '''
    ListView used for our Policies page

    Template:
    :template: `coresite/policies.html`
    '''

    model = Policy
    template_name = "core/policies.html"
    paginate_by = 10

    def get_queryset(self) -> QuerySet[Any]:
        return self.model.objects.active().order_by("-creation_date")
    