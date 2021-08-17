"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from steams import blocks


class ParallaxPage(Page):

    template = "parallax/parallax.html"

    # @todo add streamfields 
    content = StreamField(
        [
            
        ],
        null=True,
        blank=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    class Meta:  # noqa 
        verbose_name = "Parallax Page"
        verbose_name_plural = "Parallax Pages"

