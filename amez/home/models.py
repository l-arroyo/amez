from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.images.edit_handlers import FieldPanel

class HomePage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
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
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_image'),
        FieldPanel('about_us'),
        FieldPanel('about_us_image'),
        FieldPanel('event_info'),
        FieldPanel('event_image'),
    ]

    def hero_image_url(self):
        if self.hero_image:
            return self.hero_image.file.url
        return None