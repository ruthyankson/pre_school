from django.views import generic

from coresite.models import Blog

class BlogView(generic.DetailView):
    '''
    DetailView used for our Blog page
    
    **Template:**

    :template: `coresite/blog.html`
    '''
    model =  Blog
    template_name = "core/blog.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])