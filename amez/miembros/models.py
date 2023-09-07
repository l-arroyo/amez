from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
    
class Miembros(Page):

    informacion = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('informacion', classname="full"),
        InlinePanel('galeria_miembros', label="Galería de miembros"),
    ]
    
class GaleriaMiembros(Orderable):
    page = ParentalKey(Miembros, on_delete=models.CASCADE, related_name='galeria_miembros')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    nombre = models.CharField(blank=True, max_length=25)
    descripcion = RichTextField(blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('nombre'),
        FieldPanel('descripcion'),
    ]