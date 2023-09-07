from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from wagtail.images.edit_handlers import FieldPanel
from modelcluster.fields import ParentalKey

    
class HomePage(Page):
    about_us = RichTextField(blank=True)
    about_us_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    event_info = RichTextField(blank=True)
    event_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sponsors = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('about_us'),
        FieldPanel('about_us_image'),
        FieldPanel('event_info'),
        FieldPanel('event_image'),
        FieldPanel('sponsors'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    
class SponsorsGalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]