from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
    
class Evento(Page):
    concepto = RichTextField(blank=True)
    artistas = RichTextField(blank=True)
    event_info = RichTextField(blank=True)
    programacion = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('concepto', classname="full"),
        FieldPanel('artistas', classname="full"),
        InlinePanel('artistas_imgs', label="Imágenes de artistas"),
        FieldPanel('event_info', classname="full"),
        FieldPanel('programacion', classname="full"),
    ]
    
class GaleriaArtistas(Orderable):
    page = ParentalKey(Evento, on_delete=models.CASCADE, related_name='artistas_imgs')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]