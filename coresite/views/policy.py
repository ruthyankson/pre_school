from django.views import generic

from coresite.models import Policy

class PolicyView(generic.DetailView):
    '''
    DetailView used for our Policy page
    
    **Template:**

    :template: `coresite/policy.html`
    '''
    model =  Policy
    template_name = "core/policy.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])