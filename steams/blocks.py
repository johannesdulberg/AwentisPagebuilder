""" Grundgerüst mit wichtigsten Einstellungen"""


"""
class TitleAndTextBlock(blocks.StructBlock):
    Titel = blocks.CharBlock(required=True)
    
    Einstellungen=blocks.StreamBlock([ 
    ("BlockAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandUnten" , blocks.CharBlock(required=False ,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandSeiten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder  <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockInnenAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockInnenAbstandUnten" , blocks.CharBlock(required=False ,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockInnenAbstandSeiten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder  <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("HintergrundFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist weiß")),
    ("ID" ,blocks.CharBlock(required=False,help_text="Wenn man von einer anderer Seite nicht nur diese seite aufrufen, sondern auch hier hin scrollen will, kann man www.<url>/#<id> verwenden")),

    ],block_counts = {
            'BlockAbstandOben': {'max_num': 1},
            'BlockAbstandUnten': {'max_num': 1},
            'BlockAbstandSeiten': {'max_num': 1},
            "HintergrundFarbe": {'max_num': 1},
            'ID': {'max_num': 1},
            "BlockInnenAbstandOben": {'max_num': 1},
            "BlockInnenAbstandUnten": {'max_num': 1},
            "BlockInnenAbstandSeiten": {'max_num': 1},
        },required=False)
    
    
 
    

    class Meta:
        
        template = "steams/title_and_text_block.html"
        icon="edit"
        label ="Titel & Untertitel"
"""

""" Button """
"""
Button =BooleanBlock(required=False)
ButtonTitel = blocks.CharBlock(required=False)


    ],block_counts = {
            'BlockAbstandOben': {'max_num': 1},
            'BlockAbstandUnten': {'max_num': 1},
            "BlockAbstandSeiten": {'max_num': 1},
            "BlockHintergrundFarbe": {'max_num': 1},
            'BlockID': {'max_num': 1},
            'TitelAbstandUnten': {'max_num': 1},
            'UnterstrichAbstandUnten': {'max_num': 1},
            'KartenHintergrundFarbe': {'max_num': 1},
            'TitelSchriftFarbe': {'max_num': 1},
            'UntertitelSchriftFarbe': {'max_num': 1},
            'TitelSchriftgroesse': {'max_num': 1},
            'UntertitelSchriftgroesse': {'max_num': 1},
            'UnterstrichSchriftFarbe': {'max_num': 1},
            "InhaltHorizontaleAusrichtung": {'max_num': 1},
            'KartenOptik': {'max_num': 1},
            'Schatten': {'max_num': 1},
            "KartenInnenAbstandSeiten": {'max_num': 1},
            "KartenInnenAbstandObenUnten": {'max_num': 1},
            "ButtonFarbe":{'max_num': 1},
            "ButtonStil":{'max_num': 1},
            "ButtonSchriftFarbe": {'max_num': 1},
            "ButtonAbstandOben": {'max_num': 1},
            'Icon': {'max_num': 1},
        }




        class SimpleTextBlock(blocks.RichTextBlock):
    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]
    class Meta:
        template = "steams/richtext_block.html"
        icon="edit"
        label ="Simple RichText"
"""
from django.db import models
from django.db.models.deletion import SET_NULL
from wagtail.core.blocks.field_block import BooleanBlock
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel,PageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.core.blocks import URLBlock,PageChooserBlock,ChoiceBlock

class SimpleTextBlock(blocks.RichTextBlock):
    def __init__(
        self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]
    class Meta:
        template = "steams/richtext_block.html"
        icon="edit"
        label ="Simple RichText"

class RichTextBlock(blocks.StructBlock):
    rt=blocks.RichTextBlock(required=False)
    class Meta:
        template = "steams/richtext_block.html"
        icon="edit"
        label ="Full RichText"

class TitelUndTextfeld(blocks.StructBlock):
    Titel = blocks.CharBlock(required=False)
    Unterstrich = BooleanBlock(required=False,help_text="Fügt einen Kurzen Unterstrich als Designelement hinzu, der Titel und Untertitel optisch trennt")
    Textfeld = blocks.RichTextBlock(required=False)
    Button =BooleanBlock(required=False)
    ButtonTitel = blocks.CharBlock(required=False)
    ButtonSeitenwahl=blocks.PageChooserBlock(required=False,help_text="Hier kann eine Seite dieser Website ausgewählt werden")
    ButtonUrlWahl=blocks.URLBlock(required=False, help_text="Hier kann eine Url eingegeben werden z.B. roterkeil.net")
    Einstellungen=blocks.StructBlock([ 
    ("BlockAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandUnten" , blocks.CharBlock(required=False ,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandSeiten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder  <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockHintergrundFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist weiß")),
    ("BlockID" ,blocks.CharBlock(required=False,help_text="Wenn man von einer anderer Seite nicht nur diese seite aufrufen, sondern auch hier hin scrollen will, kann man www.<url>/#<id> verwenden")),
    ("TitelAbstandUnten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("TitelSchriftgroesse" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten")),
    ("UnterstrichAbstandUnten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("KartenHintergrundFarbe" , blocks.CharBlock(required=False,help_text="Falls Kart Optik erwünscht, stellt man hier die Hintergrundfarbe ein. In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f")),
    ("TitelSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Schwarz")),
    ("UnterstrichSchriftFarbe" ,blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die Primärfarbe")),
    ("InhaltHorizontaleAusrichtung" , blocks.ChoiceBlock(choices=[
    ('a', 'linksseitig'),
    ('m', 'zentriert'),
    ('e', 'rechtseitig'),
    ], icon='cup',required=False,help_text="Wenn sie den Inhalt Zentrieren wollen, geben sie m Für Mitte and. a für Anfang richtet den Text nach links aus und e für Ende nach rechts")),
    ("KartenOptik",BooleanBlock(required=False,help_text="Gibt dem Block eine Karten Optik")),
    ("Schatten",BooleanBlock(required=False,help_text="Falls Karten Optik erwünscht, kann man hier angeben, ob die Karte einen Schatten haben soll")),
    ("KartenInnenAbstandSeiten" , blocks.CharBlock(required=False,help_text="Hier kann der Abstand innerhalb der Karte angepasst werden")),
    ("KartenInnenAbstandObenUnten" , blocks.CharBlock(required=False,help_text="Hier kann der Abstand innerhalb der Karte angepasst werden")),
    ("ButtonFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die primär Farbe")),
    ("ButtonStil" , blocks.ChoiceBlock(choices=[
    ('RundeEcken', 'RundeEcken'),
    ('RundeEckenXl', 'RundeEckenXl'),
    ('KantenEcken', 'KantenEcken'),
    ('KantenEckenXl', 'KantenEckenXl'),
    ])),
    ("ButtonUnausgefuellt" , BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat")),
    ("ButtonSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß")),
    ("ButtonAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("Icon" , blocks.CharBlock(required=False,help_text="Hier wird ein Icon Oberhalb des Titels hinzugefügt. z.B. Ein Großer Haken in der Primärfarbe bi-check fs-1 text-primary Icons findet man auf https://icons.getbootstrap.com/ fs-1 bedeutet große Schrift fs-4 wäre kleiner. text-primary wäre die Hauptfarbe text-secundary die Zweitfarbe."))],
    form_classname="structblock" , help_text="Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.")
    
    
    class Meta:
        
        template = "steams/TitelUndTextfeld.html"
        icon="edit"
        label ="Titel & Textfeld"



class TitelUndUntertitel(blocks.StructBlock):
    Titel = blocks.CharBlock(required=False)
    Unterstrich = BooleanBlock(required=False,help_text="Fügt einen Kurzen Unterstrich als Designelement hinzu, der Titel und Untertitel optisch trennt")
    Untertitel = blocks.TextBlock(required=False)
    Button =BooleanBlock(required=False)
    ButtonTitel = blocks.CharBlock(required=False)
    ButtonSeitenwahl=blocks.PageChooserBlock(required=False,help_text="Hier kann eine Seite dieser Website ausgewählt werden")
    ButtonUrlWahl=blocks.URLBlock(required=False, help_text="Hier kann eine Url eingegeben werden z.B. roterkeil.net")
    Einstellungen=blocks.StructBlock([ 
    ("BlockAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandUnten" , blocks.CharBlock(required=False ,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandSeiten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder  <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockHintergrundFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist weiß")),
    ("BlockID" ,blocks.CharBlock(required=False,help_text="Wenn man von einer anderer Seite nicht nur diese seite aufrufen, sondern auch hier hin scrollen will, kann man www.<url>/#<id> verwenden")),
    ("TitelAbstandUnten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("TitelSchriftgroesse" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten")),
    ("UntertitelSchriftgroesse" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten")),
    ("UnterstrichAbstandUnten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("KartenHintergrundFarbe" , blocks.CharBlock(required=False,help_text="Falls Kart Optik erwünscht, stellt man hier die Hintergrundfarbe ein. In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f")),
    ("TitelSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Schwarz")),
    ("UntertitelSchriftFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist Schwarz")),
    ("UnterstrichSchriftFarbe" ,blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die Primärfarbe")),
    ("InhaltHorizontaleAusrichtung" , blocks.ChoiceBlock(choices=[
    ('a', 'linksseitig'),
    ('m', 'zentriert'),
    ('e', 'rechtseitig'),
    ], icon='cup',required=False,help_text="Wenn sie den Inhalt Zentrieren wollen, geben sie m Für Mitte and. a für Anfang richtet den Text nach links aus und e für Ende nach rechts")),
    ("KartenOptik",BooleanBlock(required=False,help_text="Gibt dem Block eine Karten Optik")),
    ("Schatten",BooleanBlock(required=False,help_text="Falls Karten Optik erwünscht, kann man hier angeben, ob die Karte einen Schatten haben soll")),
    ("KartenInnenAbstandSeiten" , blocks.CharBlock(required=False,help_text="Hier kann der Abstand innerhalb der Karte angepasst werden")),
    ("KartenInnenAbstandObenUnten" , blocks.CharBlock(required=False,help_text="Hier kann der Abstand innerhalb der Karte angepasst werden")),
    ("ButtonFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die primär Farbe")),
    ("ButtonStil" , blocks.ChoiceBlock(choices=[
    ('RundeEcken', 'RundeEcken'),
    ('RundeEckenXl', 'RundeEckenXl'),
    ('KantenEcken', 'KantenEcken'),
    ('KantenEckenXl', 'KantenEckenXl'),
    ])),
    ("ButtonUnausgefuellt" , BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat")),
    ("ButtonSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß")),
    ("ButtonAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("Icon" , blocks.CharBlock(required=False,help_text="Hier wird ein Icon Oberhalb des Titels hinzugefügt. z.B. Ein Großer Haken in der Primärfarbe bi-check fs-1 text-primary Icons findet man auf https://icons.getbootstrap.com/ fs-1 bedeutet große Schrift fs-4 wäre kleiner. text-primary wäre die Hauptfarbe text-secundary die Zweitfarbe."))],
    form_classname="structblock" , help_text="Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.")

    class Meta:
        
        template = "steams/TitelUndUntertitel.html"
        icon="edit"
        label ="Titel & Untertitel"


class NAVBAR(blocks.StructBlock):
    Webseitenname = blocks.TextBlock(required=True,help_text="Hier wird der Webseiten Name eingetragen, welcher in der Navigationsleiste oben rechts zu finden ist. Dieser führ im Normalfall zur Startseite.")
    WebseitennameSeitenwahl=blocks.PageChooserBlock(required=False,help_text="Wählen sie hier die Seite, auf die der Webseitenname verlinken soll.")
    WebseitennameUrlWahl= blocks.URLBlock(required=False, help_text="Falls der Webseitenname auf keine Seite dieser Webseite verlinken soll, können sie hier eine Url eingeben z.B. roterkeil.net")
    ExtraButton =BooleanBlock(required=False,help_text="Hier können sie einen zusätzlichen Button ganz links in der Navigationsleiste hinzufügen.")
    ExtraButtonTitel = blocks.CharBlock(required=False)
    ExtraButtonSeitenwahl=blocks.PageChooserBlock(required=False,help_text="Hier kann eine Seite dieser Website ausgewählt werden")
    ExtraButtonUrlWahl=blocks.URLBlock(required=False, help_text="Hier kann eine Url eingegeben werden z.B. roterkeil.net")
    Einstellungen=blocks.StructBlock([ 
    ("ExtraButtonFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die primär Farbe")),
    ("ExtraButtonStil" , blocks.ChoiceBlock(choices=[
    ('RundeEcken', 'RundeEcken'),
    ('RundeEckenXl', 'RundeEckenXl'),
    ('KantenEcken', 'KantenEcken'),
    ('KantenEckenXl', 'KantenEckenXl'),
    ])),
    ("ExtraButtonUnausgefuellt" , BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat")),
    ("ExtraButtonSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß")),
    ("NavigationsleisteZentriert" , BooleanBlock(required=False,help_text="Wenn dieses Kästchen ausgewählt ist, werden alle Reiter in der Mitte der Navigationsleiste zentriert"))],
    form_classname="structblock" , help_text="Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.")
    NavigationsleistenReiter = blocks.ListBlock(
        blocks.StructBlock([
            ("ReiterTitel",blocks.CharBlock(required=True)),
            ("ReiterSeitenWahl", blocks.PageChooserBlock(required=False)),
            ("ReiterUrlWahl", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
        ])
    )

    class Meta:
        template = "steams/NAVBAR.html"
        icon="edit"
        label ="Navigationsleiste"





class MASTERHEAD(blocks.StructBlock):
    Titel = blocks.CharBlock(required=True)
    Unterstrich = BooleanBlock(required=False,help_text="Fügt einen Kurzen Unterstrich als Designelement hinzu, der Titel und Untertitel optisch trennt")
    Untertitel = blocks.TextBlock(required=False)
    Hintergrundbild = ImageChooserBlock(required=True)
    Button =BooleanBlock(required=False)
    ButtonTitel = blocks.CharBlock(required=False)
    ButtonSeitenwahl=blocks.PageChooserBlock(required=False,help_text="Hier kann eine Seite dieser Website ausgewählt werden")
    ButtonUrlWahl=blocks.URLBlock(required=False, help_text="Hier kann eine Url eingegeben werden z.B. roterkeil.net")
    
    Einstellungen=blocks.StructBlock([ 
    ("HintergrundbildXPosition" ,blocks.CharBlock(required=False,help_text="Ist das bild in Verschiedenen Browserfenstergrößen durchschnittlich zu weit unten(Kopf einer Person nicht sichtbar wenn er im Bild oben ist), kann man hier eine Zahl zwischen 0 und 100 eigeben. 0 würde dafür sorgen, dass das bild immer oben anfängt. Default=50")),
    ("HintergrundbildYPosition" , blocks.CharBlock(required=False ,help_text="Ist das bild in Verschiedenen Browserfenstergrößen durchschnittlich zu weitnach rechts verrückt, kann man hier eine Zahl zwischen 0 und 100 eigeben. 0 würde dafür sorgen, dass das bild immer links anfängt.Default=50")),
    ("HintergrundbildGroesse" , blocks.ChoiceBlock(choices=[
    ('sehrkleinP', 'sehrklein%'), 
    ('kleinP', 'klein%'),
    ('grossP', 'gross%'),
    ('sehrkleinA', 'sehrkleinAbsolut'),
    ('kleinA', 'kleinAbsolut'),
    ('grossA', 'grossAbsolut'),
    ], icon='cup',required=False,help_text="sehrklein% entspricht etwa 20% der zu verfügung stehenden höhe.Klein etwa 30% Groß etwa 60%. SehrkleinAbsolut etwa 200px. KleinAbsolut etwa 380px. GroßAbsolut etwa 700px." )),
    ("HintergrundbildFixiert" ,BooleanBlock(required=False,help_text="Fixiert das Hintergrund Bild, sodass es sich beim Scrollen nicht bewegt")),
    ("TitelAbstandUnten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("TitelSchriftgroesse" , blocks.CharBlock(required=False,help_text="fs- gefolgt von einer Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten z.B. fs-1")),
    ("UntertitelSchriftgroesse" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten")),
    ("UnterstrichAbstandUnten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("TitelSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Schwarz")),
    ("UntertitelSchriftFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist Schwarz")),
    ("UnterstrichSchriftFarbe" ,blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die Primärfarbe")),
    ("InhaltHorizontaleAusrichtung" , blocks.ChoiceBlock(choices=[
    ('a', 'linksseitig'),
    ('m', 'zentriert'),
    ('e', 'rechtseitig'),
    ], icon='cup',required=False,help_text="Wollen sie ihren Text linksbündig können sie hier z.B. linksseitig auswählen.")),
    #("InhaltInnenAbstandSeiten" , blocks.CharBlock(required=False,help_text="Hier kann der Abstand innerhalb der Karte angepasst werden")),
    #("InhaltInnenAbstandObenUnten" , blocks.CharBlock(required=False,help_text="Hier kann der Abstand innerhalb der Karte angepasst werden")),
    ("ButtonFarbe" , blocks.CharBlock(required=False,help_text="Hier kann z.B. primary angegeben werden für ein Button in der Hauptfarbe der Website secundary succsess danger warning info light und dark sind weitere verfügbare Farben")),
    ("ButtonStil" , blocks.ChoiceBlock(choices=[
    ('RundeEcken', 'RundeEcken'),
    ('RundeEckenXl', 'RundeEckenXl'),
    ('KantenEcken', 'KantenEcken'),
    ('KantenEckenXl', 'KantenEckenXl'),
    ])),
    ("ButtonUnausgefuellt" , BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat")),
    ("ButtonSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß")),
    ("ButtonAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("Icon" , blocks.CharBlock(required=False,help_text="Hier wird ein Icon Oberhalb des Titels hinzugefügt. z.B. Ein Großer Haken in der Primärfarbe bi-check fs-1 text-primary Icons findet man auf https://icons.getbootstrap.com/ fs-1 bedeutet große Schrift fs-4 wäre kleiner. text-primary wäre die Hauptfarbe text-secundary die Zweitfarbe."))],
    form_classname="structblock" , help_text="Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.")
    

    class Meta:
        template = "steams/MASTERHEAD.html"
        icon="edit"
        label ="Kopfzeile/Header"


"""
class SERVICES(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    Service1Header = blocks.TextBlock(required=True)
    Service1Subtitle = blocks.TextBlock(required=True)
    Service2Header = blocks.TextBlock(required=True)
    Service2Subtitle = blocks.TextBlock(required=True)
    Service3Header = blocks.TextBlock(required=True)
    Service3Subtitle = blocks.TextBlock(required=True)
    Service4Header = blocks.TextBlock(required=True)
    Service4Subtitle = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/SERVICES.html"
        icon="edit"
        label ="SERVICES"
"""


class GALLERIE(blocks.StructBlock):
    Image1 = ImageChooserBlock(required=True)
    Image2 = ImageChooserBlock(required=True)
    Image3 = ImageChooserBlock(required=True)
    Image4 = ImageChooserBlock(required=True)
    Image5 = ImageChooserBlock(required=True)
    Image6 = ImageChooserBlock(required=True)
    Image1Thumbnail = ImageChooserBlock(required=True)
    Image2Thumbnail = ImageChooserBlock(required=True)
    Image3Thumbnail = ImageChooserBlock(required=True)
    Image4Thumbnail = ImageChooserBlock(required=True)
    Image5Thumbnail = ImageChooserBlock(required=True)
    Image6Thumbnail = ImageChooserBlock(required=True)
    Image1Categorie = blocks.TextBlock(required=True)
    Image1Project = blocks.TextBlock(required=True)
    Image2Categorie = blocks.TextBlock(required=True)
    Image2Project = blocks.TextBlock(required=True)
    Image3Categorie = blocks.TextBlock(required=True)
    Image3Project = blocks.TextBlock(required=True)
    Image4Categorie = blocks.TextBlock(required=True)
    Image4Project = blocks.TextBlock(required=True)
    Image5Categorie = blocks.TextBlock(required=True)
    Image5Project = blocks.TextBlock(required=True)
    Image6Categorie = blocks.TextBlock(required=True)
    Image6Project = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/GALLERIE.html"
        icon="edit"
        label ="GALLERIE"

class SERVICES(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    Service1Header = blocks.TextBlock(required=True)
    Service1Subtitle = blocks.TextBlock(required=True)
    Service2Header = blocks.TextBlock(required=True)
    Service2Subtitle = blocks.TextBlock(required=True)
    Service3Header = blocks.TextBlock(required=True)
    Service3Subtitle = blocks.TextBlock(required=True)
    Service4Header = blocks.TextBlock(required=True)
    Service4Subtitle = blocks.TextBlock(required=True)

    class Meta:
        template = "steams/SERVICES.html"
        icon="edit"
        label ="SERVICES"

class CONTACT(blocks.StructBlock):
    HEADER = blocks.TextBlock(required=True)
    headerSubtitle = blocks.TextBlock(required=True)
    button = blocks.TextBlock(required=True)
    HintergrundBild = ImageChooserBlock(required=False)
    AbstandNachObenUnten=blocks.TextBlock(required=False)
    HintergrundFarbe=blocks.TextBlock(required=False)
    SchriftFarbe=blocks.TextBlock(required=False)
    

    class Meta:
        template = "steams/CONTACT.html"
        icon="edit"
        label ="CONTACT"

class VideoHeader(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    subtitle = blocks.TextBlock(required=True)
    button_page=blocks.PageChooserBlock(required=False)
    button_url=blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")
    BUTTON= blocks.TextBlock(required=False)

    class Meta:
        template = "steams/VideoHeader.html"
        icon="edit"
        label ="VideoHeader"

class CardPicture(blocks.StructBlock):
    title = blocks.TextBlock(required=True)
    subtitle = blocks.TextBlock(required=True)
    btn = blocks.TextBlock(required=False)
    image = ImageChooserBlock(required=True)
    position = blocks.TextBlock(required=False)
    rounded=BooleanBlock(required=False)
    AbstandNachUnten = blocks.CharBlock(required=False)
    AbstandNachOben = blocks.CharBlock(required=False)
    AbstandSeiten = blocks.CharBlock(required=False,help_text="Default=0")
    button_url=blocks.URLBlock(required=False)

    class Meta:
        template = "steams/CardPicture.html"
        icon="edit"
        label ="CardPicture"

class ThreeImagesCallToAction(blocks.StructBlock):
    HintergrundFarbe=blocks.TextBlock(required=True)
    BackgroundImage = ImageChooserBlock(required=False)
    title1 = blocks.TextBlock(required=True)
    title2 = blocks.TextBlock(required=True)
    title3 = blocks.TextBlock(required=True)
    subtitle1 = blocks.TextBlock(required=True)
    subtitle2 = blocks.TextBlock(required=True)
    subtitle3 = blocks.TextBlock(required=True)
    info1 = blocks.TextBlock(required=True)
    info2 = blocks.TextBlock(required=True)
    info3 = blocks.TextBlock(required=True)
    btn1 = blocks.TextBlock(required=False)
    btn2 = blocks.TextBlock(required=False)
    btn3 = blocks.TextBlock(required=False)
    image1 = ImageChooserBlock(required=True)
    image2 = ImageChooserBlock(required=True)
    image3 = ImageChooserBlock(required=True)

    class Meta:
        template = "steams/ThreeImagesCallToAction.html"
        icon="edit"
        label ="ThreeImagesCallToAction"

class CardBlock(blocks.StructBlock):
    
    Einstellungen=blocks.StructBlock([ 
    ("BlockAbstandOben" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandUnten" , blocks.CharBlock(required=False ,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockAbstandSeiten" , blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder  <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
    ("BlockHintergrundFarbe" , blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist weiß")),
    ("BlockID" ,blocks.CharBlock(required=False,help_text="Wenn man von einer anderer Seite nicht nur diese seite aufrufen, sondern auch hier hin scrollen will, kann man www.<url>/#<id> verwenden")),
    ("HintergrundBild" , ImageChooserBlock(required=False,help_text="Setzt die Mindesthöhe auf 700px!")),
    ("RundeBilder",BooleanBlock(required=False, help_text="Die Bilder innerhalb der Blöcke werden rund.")),
    ("FarbeRandUmBilder",blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist grau")),
    ("GrauerRand",BooleanBlock(required=False,help_text="Hiermit kann ein grauer Rand um die Innenblöcke erzeugt werden" )),
    ("Schatten", BooleanBlock(required=False)),
    ("AbstandZwischenBildern", blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=mx-3 ")),
    ("Breakpoint", blocks.CharBlock(required=False,help_text="Bei welcher größe Umgebrochen wird Default sm")),
    ],
    form_classname="structblock" , help_text="Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt."),
    
    InnenBloecke = blocks.ListBlock(
        blocks.StructBlock([
            ("Bild",ImageChooserBlock(required=False)),
            ("Textfeld",blocks.RichTextBlock(required=False)),  
            ("Button" ,BooleanBlock(required=False,help_text="Hier kann eine Button hinzugefügt werden")),
            ("ButtonTitel",  blocks.CharBlock(required=False)),
            ("ButtonSeitenwahl",blocks.PageChooserBlock(required=False,help_text="Hier kann eine Seite dieser Website ausgewählt werden")),
            ("ButtonUrlWahl", blocks.URLBlock(required=False, help_text="Hier kann eine Url eingegeben werden z.B. roterkeil.net")),
            ("Einstellungen" ,blocks.StructBlock([ 
            ("TextAbstandSeiten",blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")), 
            ("TextAbstandOben", blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")), 
            ("TextAbstandUnten", blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")), 
            ("HintergrundFarbeKarte",blocks.CharBlock(required=False,help_text="Farbe in Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f")),
            ("Icon",blocks.CharBlock(required=False,help_text="Hier wird ein Icon statt den Bildern verwender werden. z.B. Ein Großer Haken in der Primärfarbe bi-check fs-1 text-primary Icons findet man auf https://icons.getbootstrap.com/ fs-1 bedeutet große Schrift fs-4 wäre kleiner. text-primary wäre die Hauptfarbe text-secundary die Zweitfarbe.")),
            ("ButtonFarbe" , blocks.CharBlock(required=False,help_text="Hier kann z.B. primary angegeben werden für ein Button in der Hauptfarbe der Website secundary succsess danger warning info light und dark sind weitere verfügbare Farben")),
            ("ButtonStil" , blocks.ChoiceBlock(choices=[
            ('RundeEcken', 'RundeEcken'),
            ('RundeEckenXl', 'RundeEckenXl'),
            ('KantenEcken', 'KantenEcken'),
            ('KantenEckenXl', 'KantenEckenXl'),
            ] ,icon='cup',required=False)),
            ("ButtonUnausgefuellt" , BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat")),
            ("ButtonSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß")),
            ("ButtonAbstandUnten" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
            ("ButtonLang", BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button die volle länge des Textes einnimmt")),
            ("ButtonHorizontaleAusrichtung" , blocks.ChoiceBlock(choices=[
            ('a', 'linksseitig'),
            ('m', 'zentriert'),
            ('e', 'rechtseitig'),
            ], icon='cup',required=False,help_text="Ausrichtungsmöglichkeiten für den Text")),
            
            ],
            form_classname="structblock" , help_text="Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt."))
            
        ]))
    
    class Meta:
        template = "steams/CardBlock.html"
        icon="edit"
        label ="BloeckeNebeneinander"


class SlideShow(blocks.StructBlock):
    image1 = ImageChooserBlock(required=True)
    image2 = ImageChooserBlock(required=True)
    image3 = ImageChooserBlock(required=True)
    title1 = blocks.CharBlock(required=False)
    title2 = blocks.CharBlock(required=False)
    title3 = blocks.CharBlock(required=False)
    info1 = blocks.TextBlock(required=False)
    info2 = blocks.TextBlock(required=False)
    info3 = blocks.TextBlock(required=False)


    class Meta:
        template = "steams/SlideShow.html"
        icon="edit"
        label ="SlideShow"
class ClickableCardBlock(blocks.StructBlock):
    """Cards with image and text and buttons"""
    AbstandNachObenUnten = blocks.CharBlock(required=False)
    HintergrundFarbe = blocks.CharBlock(required=False)
    SchriftFarbe = blocks.CharBlock(required=False)
    AbstandZwischenBildern=BooleanBlock(required=False)
    AbstandSeiten = blocks.CharBlock(required=False,help_text="Default=0")
    Klein =BooleanBlock(required=False)
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("image",ImageChooserBlock(required=False)),            
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False, help_text="If the button page above is selected, that will be used first.")),
            ("ButtonTitle",blocks.TextBlock(required=False)),
            
        ])
    )
    class Meta:
        template = "steams/ClickableCardBlock.html"
        icon="edit"
        label ="ClickableCardBlock"


"""class Parallax(blocks.StructBlock):
    AbstandNachObenUnten = blocks.CharBlock(required=False,help_text="Default=0")
    AbstandSeiten = blocks.CharBlock(required=False,help_text="Default=0")
    HintergrundFarbe = blocks.CharBlock(required=False)
    SchriftFarbe = blocks.CharBlock(required=False)
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("image",ImageChooserBlock(required=False)),            
        ])
    )
    class Meta:
        template = "steams/Parallax.html"
        icon="edit"
        label ="Parralax"""

class Parallax(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    titleTop = blocks.CharBlock(required=False)
    titleLeft = blocks.CharBlock(required=False)
    AbstandNachObenUnten = blocks.CharBlock(required=False,help_text="Default=0")
    AbstandSeiten = blocks.CharBlock(required=False,help_text="Default=0")
    HintergrundFarbe = blocks.CharBlock(required=False)
    SchriftFarbe = blocks.CharBlock(required=False)
    image=ImageChooserBlock(required=False)
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("image",ImageChooserBlock(required=False)),            
        ])
    )
    class Meta:
        template = "steams/Parallax.html"
        icon="edit"
        label ="Parralax"


class ResponsiveGallery(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("Bild",ImageChooserBlock(required=False)),            
        ])
    )
    class Meta:
        template = "steams/ResponsiveGallery.html"
        icon="edit"
        label ="ResponsiveGallery"

class ParallaxBild(blocks.StructBlock):
    HintergrundBild= ImageChooserBlock(required=True)
    Bildhoehe = blocks.CharBlock(required=True,help_text="1-200. 100 wäre Quadratisch")
    Bildverschiebung = blocks.CharBlock(required=True,help_text="-20 - 20. Anfängliche Verschiebung des Bildes aus dem Zentrum raus")
    class Meta:
        template="steams/ParallaxBild.html"
        icon="edit"
        label="ParallaxBild"

"""
            ("Einstellungen" ,blocks.StructBlock([ 
            ("TextAbstandSeiten",blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")), 
            ("TextAbstandOben", blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")), 
            ("TextAbstandUnten", blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")), 
            ("HintergrundFarbeKarte",blocks.CharBlock(required=False,help_text="Farbe in Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f")),
            ("Icon",blocks.CharBlock(required=False,help_text="Icons statt bilder")),
            ("ButtonFarbe" , blocks.CharBlock(required=False,help_text="Hier kann z.B. primary angegeben werden für ein Button in der Hauptfarbe der Website secundary succsess danger warning info light und dark sind weitere verfügbare Farben")),
            ("ButtonStil" , blocks.ChoiceBlock(choices=[
            ('RundeEcken', 'RundeEcken'),
            ('RundeEckenXl', 'RundeEckenXl'),
            ('KantenEcken', 'KantenEcken'),
            ('KantenEckenXl', 'KantenEckenXl'),
            ])),
            ("ButtonUnausgefuellt" , BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat")),
            ("ButtonSchriftFarbe", blocks.CharBlock(required=False,help_text="In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß")),
            ("ButtonAbstandUnten" ,blocks.CharBlock(required=False,help_text="Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ")),
            ("ButtonKurz", BooleanBlock(required=False,help_text="Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat")),
            ("ButtonHorizontaleAusrichtung" , blocks.ChoiceBlock(choices=[
            ('a', 'linksseitig'),
            ('m', 'zentriert'),
            ('e', 'rechtseitig'),
            ], icon='cup',required=False,help_text="Wenn sie den Inhalt Zentrieren wollen, geben sie m Für Mitte and. a für Anfang richtet den Text nach links aus und e für Ende nach rechts")),
            
            ],
            form_classname="structblock" , help_text="Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt."))
            """