from django.views import generic

class AboutView(generic.TemplateView):
    '''
    Template used for our About page

    Template

    :template: `coresite/about.html`

    '''
    template_name = "coresite/about.html"