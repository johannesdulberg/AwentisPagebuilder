# Generated by Django 3.2.6 on 2021-08-10 18:41

from django.db import migrations
import steams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0003_alter_flexpage_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('text', wagtail.core.blocks.TextBlock(required=True)), ('AbstandNachObenUnten', wagtail.core.blocks.CharBlock(required=False))], classname='text_and_title')), ('full_richtext', steams.blocks.RichTextBlock()), ('simple_richtext', steams.blocks.SimpleTextBlock()), ('NAVABR', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('MASTERHEAD', wagtail.core.blocks.StructBlock([('HEADER', wagtail.core.blocks.TextBlock(required=True)), ('SUBTITLE', wagtail.core.blocks.TextBlock(required=True)), ('BUTTON', wagtail.core.blocks.TextBlock(required=False)), ('MasterImage', wagtail.images.blocks.ImageChooserBlock(required=True)), ('klein', wagtail.core.blocks.BooleanBlock(required=False))])), ('ABOUT', wagtail.core.blocks.StructBlock([('HEADER', wagtail.core.blocks.TextBlock(required=True)), ('SUBTITLE', wagtail.core.blocks.TextBlock(required=True)), ('BUTTON', wagtail.core.blocks.TextBlock(required=True))])), ('SERVICES', wagtail.core.blocks.StructBlock([('HEADER', wagtail.core.blocks.TextBlock(required=True)), ('Service1Header', wagtail.core.blocks.TextBlock(required=True)), ('Service1Subtitle', wagtail.core.blocks.TextBlock(required=True)), ('Service2Header', wagtail.core.blocks.TextBlock(required=True)), ('Service2Subtitle', wagtail.core.blocks.TextBlock(required=True)), ('Service3Header', wagtail.core.blocks.TextBlock(required=True)), ('Service3Subtitle', wagtail.core.blocks.TextBlock(required=True)), ('Service4Header', wagtail.core.blocks.TextBlock(required=True)), ('Service4Subtitle', wagtail.core.blocks.TextBlock(required=True))])), ('GALLERIE', wagtail.core.blocks.StructBlock([('Image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image4', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image5', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image6', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image1Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image2Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image3Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image4Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image5Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image6Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image1Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image1Project', wagtail.core.blocks.TextBlock(required=True)), ('Image2Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image2Project', wagtail.core.blocks.TextBlock(required=True)), ('Image3Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image3Project', wagtail.core.blocks.TextBlock(required=True)), ('Image4Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image4Project', wagtail.core.blocks.TextBlock(required=True)), ('Image5Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image5Project', wagtail.core.blocks.TextBlock(required=True)), ('Image6Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image6Project', wagtail.core.blocks.TextBlock(required=True))])), ('CONTACT', wagtail.core.blocks.StructBlock([('HEADER', wagtail.core.blocks.TextBlock(required=True)), ('headerSubtitle', wagtail.core.blocks.TextBlock(required=True)), ('button', wagtail.core.blocks.TextBlock(required=True))])), ('NavbarCentered', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=True)), ('site1', wagtail.core.blocks.TextBlock(required=True)), ('site2', wagtail.core.blocks.TextBlock(required=True)), ('site3', wagtail.core.blocks.TextBlock(required=True)), ('site4', wagtail.core.blocks.TextBlock(required=True))])), ('VideoHeader', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('subtitle', wagtail.core.blocks.TextBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('BUTTON', wagtail.core.blocks.TextBlock(required=False))])), ('CardPicture', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=True)), ('subtitle', wagtail.core.blocks.TextBlock(required=True)), ('btn', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('position', wagtail.core.blocks.TextBlock(required=False)), ('rounded', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandNachUnten', wagtail.core.blocks.CharBlock(required=False)), ('AbstandNachOben', wagtail.core.blocks.CharBlock(required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])), ('ThreeImagesCallToAction', wagtail.core.blocks.StructBlock([('title1', wagtail.core.blocks.TextBlock(required=True)), ('title2', wagtail.core.blocks.TextBlock(required=True)), ('title3', wagtail.core.blocks.TextBlock(required=True)), ('subtitle1', wagtail.core.blocks.TextBlock(required=True)), ('subtitle2', wagtail.core.blocks.TextBlock(required=True)), ('subtitle3', wagtail.core.blocks.TextBlock(required=True)), ('info1', wagtail.core.blocks.TextBlock(required=True)), ('info2', wagtail.core.blocks.TextBlock(required=True)), ('info3', wagtail.core.blocks.TextBlock(required=True)), ('btn1', wagtail.core.blocks.TextBlock(required=False)), ('btn2', wagtail.core.blocks.TextBlock(required=False)), ('btn3', wagtail.core.blocks.TextBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('CardBlock', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('id', wagtail.core.blocks.CharBlock(required=False)), ('AbstandNachObenUnten', wagtail.core.blocks.CharBlock(required=False)), ('HintergrundFarbe', wagtail.core.blocks.CharBlock(required=False)), ('SchriftFarbe', wagtail.core.blocks.CharBlock(required=False)), ('rounded', wagtail.core.blocks.BooleanBlock(required=False)), ('CardOptic', wagtail.core.blocks.BooleanBlock(required=False)), ('Schatten', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandZwischenBildern', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('HintergrundFarbeKarte', wagtail.core.blocks.CharBlock(required=False)), ('icon', wagtail.core.blocks.CharBlock(required=False)), ('text', wagtail.core.blocks.TextBlock(required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('ButtonText', wagtail.core.blocks.TextBlock(required=False))])))])), ('SlideShow', wagtail.core.blocks.StructBlock([('image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title1', wagtail.core.blocks.CharBlock(required=False)), ('title2', wagtail.core.blocks.CharBlock(required=False)), ('title3', wagtail.core.blocks.CharBlock(required=False)), ('info1', wagtail.core.blocks.TextBlock(required=False)), ('info2', wagtail.core.blocks.TextBlock(required=False)), ('info3', wagtail.core.blocks.TextBlock(required=False))])), ('ClickableCardBlock', wagtail.core.blocks.StructBlock([('AbstandNachObenUnten', wagtail.core.blocks.CharBlock(required=False)), ('HintergrundFarbe', wagtail.core.blocks.CharBlock(required=False)), ('SchriftFarbe', wagtail.core.blocks.CharBlock(required=False)), ('AbstandZwischenBildern', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('ButtonTitle', wagtail.core.blocks.TextBlock(required=False))])))])), ('Parralax', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('AbstandNachObenUnten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('HintergrundFarbe', wagtail.core.blocks.CharBlock(required=False)), ('SchriftFarbe', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
