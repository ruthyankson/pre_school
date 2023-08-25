from django.db import models
from utils.model import MyModel

from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel

from ckeditor.fields import RichTextField

class Blog(ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel, MyModel):

    class Meta:
        verbose_name_plural = "Blogs"

    body = RichTextField()
    