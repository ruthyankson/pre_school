from django.views import generic

from coresite.models import Event

class EventView(generic.DetailView):
    '''
    DetailView used for our Event page
    
    **Template:**

    :template: `coresite/event.html`
    '''
    model =  Event
    template_name = "core/event.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])