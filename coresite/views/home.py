from django.views import generic

class HomeView(generic.TemplateView):
    '''
    Template used for our home page

    Template

    :template: `coresite/index.html`

    '''
    template_name = "coresite/index.html"