from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

class EventPage(Page):
    informacion = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('informacion', classname="full"),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []
