from django.db import models
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class EventBlock(blocks.StructBlock):
    event_name = blocks.CharBlock(required=True, max_length=255, label="Nombre del evento")
    event_content = blocks.RichTextBlock(required=True, label="Contenido de la sección")

    class Meta:
        icon = 'doc-full'
        label = "Añadir evento"

class EventPage(Page):
    
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    próximos_eventos = StreamField([
        ('event', EventBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('próximos_eventos'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

    def hero_image_url(self):
        if self.hero_image:
            return self.hero_image.file.url
        return None