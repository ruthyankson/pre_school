from django.db.models.query import QuerySet
from django.views import generic

from coresite.models import Blog

class BlogsView(generic.ListView):
    '''
    ListView used for our Blogs page

    Template:
    :template: `coresite/blogs.html`
    '''

    model = Blog
    template_name = "core/blogs.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-creation_date")
    