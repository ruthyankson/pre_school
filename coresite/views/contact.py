from django.views import generic

from coresite.models import Contact

from coresite.forms import ContactForm

class ContactView(generic.FormView):

    '''
    FormView used for Contact page
    
    **Template:**

    :template:`core/contact.html`
    '''
    template_name = "coresite/contact.html"
    form_class = ContactForm
    success_url = "/"