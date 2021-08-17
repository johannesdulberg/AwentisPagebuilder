"""Flexible page."""
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel,MultiFieldPanel,PageChooserPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel


from steams import blocks


class FlexPage(Page):
    """Flexibile page class."""

    template = "flex/flex_page.html"

    # @todo add streamfields 
    content = StreamField(
        [
            ("TitelUndUntertitel",blocks.TitelUndUntertitel()),
            ("TitelUndTextfeld",blocks.TitelUndTextfeld()),
            
            ("NAVBAR",blocks.NAVBAR()),
            ("MASTERHEAD",blocks.MASTERHEAD()),
            
            
            ("GALLERIE",blocks.GALLERIE()),
            ("CONTACT",blocks.CONTACT()),
            
            ("VideoHeader",blocks.VideoHeader()),
            ("CardPicture",blocks.CardPicture()),
            ("ThreeImagesCallToAction",blocks.ThreeImagesCallToAction()),
            ("CardBlock",blocks.CardBlock()),
            ("SlideShow",blocks.SlideShow()),
            ("ClickableCardBlock",blocks.ClickableCardBlock()),
            ("Parralax",blocks.Parallax()),
            ("ResponsiveGallery",blocks.ResponsiveGallery()),
            ("ParallaxBild",blocks.ParallaxBild()),
        ],
        null=True,
        blank=True
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
        

    ]

    class Meta:  # noqa 
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

