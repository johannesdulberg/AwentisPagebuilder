# Generated by Django 3.2.6 on 2021-08-17 03:52

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0007_auto_20210815_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('TitelUndUntertitel', wagtail.core.blocks.StructBlock([('Titel', wagtail.core.blocks.CharBlock(required=False)), ('Unterstrich', wagtail.core.blocks.BooleanBlock(help_text='Fügt einen Kurzen Unterstrich als Designelement hinzu, der Titel und Untertitel optisch trennt', required=False)), ('Untertitel', wagtail.core.blocks.TextBlock(required=False)), ('Button', wagtail.core.blocks.BooleanBlock(required=False)), ('ButtonTitel', wagtail.core.blocks.CharBlock(required=False)), ('ButtonSeitenwahl', wagtail.core.blocks.PageChooserBlock(help_text='Hier kann eine Seite dieser Website ausgewählt werden', required=False)), ('ButtonUrlWahl', wagtail.core.blocks.URLBlock(help_text='Hier kann eine Url eingegeben werden z.B. roterkeil.net', required=False)), ('Einstellungen', wagtail.core.blocks.StructBlock([('BlockAbstandOben', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('BlockAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('BlockAbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder  <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('BlockHintergrundFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist weiß', required=False)), ('BlockID', wagtail.core.blocks.CharBlock(help_text='Wenn man von einer anderer Seite nicht nur diese seite aufrufen, sondern auch hier hin scrollen will, kann man www.<url>/#<id> verwenden', required=False)), ('TitelAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('TitelSchriftgroesse', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten', required=False)), ('UntertitelSchriftgroesse', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten', required=False)), ('UnterstrichAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('KartenHintergrundFarbe', wagtail.core.blocks.CharBlock(help_text='Falls Kart Optik erwünscht, stellt man hier die Hintergrundfarbe ein. In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f', required=False)), ('TitelSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Schwarz', required=False)), ('UntertitelSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist Schwarz', required=False)), ('UnterstrichSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die Primärfarbe', required=False)), ('InhaltHorizontaleAusrichtung', wagtail.core.blocks.ChoiceBlock(choices=[('a', 'linksseitig'), ('m', 'zentriert'), ('e', 'rechtseitig')], help_text='Wenn sie den Inhalt Zentrieren wollen, geben sie m Für Mitte and. a für Anfang richtet den Text nach links aus und e für Ende nach rechts', icon='cup', required=False)), ('KartenOptik', wagtail.core.blocks.BooleanBlock(help_text='Gibt dem Block eine Karten Optik', required=False)), ('Schatten', wagtail.core.blocks.BooleanBlock(help_text='Falls Karten Optik erwünscht, kann man hier angeben, ob die Karte einen Schatten haben soll', required=False)), ('KartenInnenAbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Hier kann der Abstand innerhalb der Karte angepasst werden', required=False)), ('KartenInnenAbstandObenUnten', wagtail.core.blocks.CharBlock(help_text='Hier kann der Abstand innerhalb der Karte angepasst werden', required=False)), ('ButtonFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die primär Farbe', required=False)), ('ButtonStil', wagtail.core.blocks.ChoiceBlock(choices=[('RundeEcken', 'RundeEcken'), ('RundeEckenXl', 'RundeEckenXl'), ('KantenEcken', 'KantenEcken'), ('KantenEckenXl', 'KantenEckenXl')])), ('ButtonUnausgefuellt', wagtail.core.blocks.BooleanBlock(help_text='Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat', required=False)), ('ButtonSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß', required=False)), ('ButtonAbstandOben', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('Icon', wagtail.core.blocks.CharBlock(help_text='Hier wird ein Icon Oberhalb des Titels hinzugefügt. z.B. Ein Großer Haken in der Primärfarbe bi-check fs-1 text-primary Icons findet man auf https://icons.getbootstrap.com/ fs-1 bedeutet große Schrift fs-4 wäre kleiner. text-primary wäre die Hauptfarbe text-secundary die Zweitfarbe.', required=False))], form_classname='structblock', help_text='Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.'))])), ('TitelUndTextfeld', wagtail.core.blocks.StructBlock([('Titel', wagtail.core.blocks.CharBlock(required=False)), ('Unterstrich', wagtail.core.blocks.BooleanBlock(help_text='Fügt einen Kurzen Unterstrich als Designelement hinzu, der Titel und Untertitel optisch trennt', required=False)), ('Textfeld', wagtail.core.blocks.RichTextBlock(required=False)), ('Button', wagtail.core.blocks.BooleanBlock(required=False)), ('ButtonTitel', wagtail.core.blocks.CharBlock(required=False)), ('ButtonSeitenwahl', wagtail.core.blocks.PageChooserBlock(help_text='Hier kann eine Seite dieser Website ausgewählt werden', required=False)), ('ButtonUrlWahl', wagtail.core.blocks.URLBlock(help_text='Hier kann eine Url eingegeben werden z.B. roterkeil.net', required=False)), ('Einstellungen', wagtail.core.blocks.StructBlock([('BlockAbstandOben', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('BlockAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('BlockAbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder  <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('BlockHintergrundFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist weiß', required=False)), ('BlockID', wagtail.core.blocks.CharBlock(help_text='Wenn man von einer anderer Seite nicht nur diese seite aufrufen, sondern auch hier hin scrollen will, kann man www.<url>/#<id> verwenden', required=False)), ('TitelAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('TitelSchriftgroesse', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten', required=False)), ('UnterstrichAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('KartenHintergrundFarbe', wagtail.core.blocks.CharBlock(help_text='Falls Kart Optik erwünscht, stellt man hier die Hintergrundfarbe ein. In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f', required=False)), ('TitelSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Schwarz', required=False)), ('UnterstrichSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die Primärfarbe', required=False)), ('InhaltHorizontaleAusrichtung', wagtail.core.blocks.ChoiceBlock(choices=[('a', 'linksseitig'), ('m', 'zentriert'), ('e', 'rechtseitig')], help_text='Wenn sie den Inhalt Zentrieren wollen, geben sie m Für Mitte and. a für Anfang richtet den Text nach links aus und e für Ende nach rechts', icon='cup', required=False)), ('KartenOptik', wagtail.core.blocks.BooleanBlock(help_text='Gibt dem Block eine Karten Optik', required=False)), ('Schatten', wagtail.core.blocks.BooleanBlock(help_text='Falls Karten Optik erwünscht, kann man hier angeben, ob die Karte einen Schatten haben soll', required=False)), ('KartenInnenAbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Hier kann der Abstand innerhalb der Karte angepasst werden', required=False)), ('KartenInnenAbstandObenUnten', wagtail.core.blocks.CharBlock(help_text='Hier kann der Abstand innerhalb der Karte angepasst werden', required=False)), ('ButtonFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die primär Farbe', required=False)), ('ButtonStil', wagtail.core.blocks.ChoiceBlock(choices=[('RundeEcken', 'RundeEcken'), ('RundeEckenXl', 'RundeEckenXl'), ('KantenEcken', 'KantenEcken'), ('KantenEckenXl', 'KantenEckenXl')])), ('ButtonUnausgefuellt', wagtail.core.blocks.BooleanBlock(help_text='Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat', required=False)), ('ButtonSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß', required=False)), ('ButtonAbstandOben', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('Icon', wagtail.core.blocks.CharBlock(help_text='Hier wird ein Icon Oberhalb des Titels hinzugefügt. z.B. Ein Großer Haken in der Primärfarbe bi-check fs-1 text-primary Icons findet man auf https://icons.getbootstrap.com/ fs-1 bedeutet große Schrift fs-4 wäre kleiner. text-primary wäre die Hauptfarbe text-secundary die Zweitfarbe.', required=False))], form_classname='structblock', help_text='Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.'))])), ('NAVBAR', wagtail.core.blocks.StructBlock([('Webseitenname', wagtail.core.blocks.TextBlock(help_text='Hier wird der Webseiten Name eingetragen, welcher in der Navigationsleiste oben rechts zu finden ist. Dieser führ im Normalfall zur Startseite.', required=True)), ('WebseitennameSeitenwahl', wagtail.core.blocks.PageChooserBlock(help_text='Wählen sie hier die Seite, auf die der Webseitenname verlinken soll.', required=False)), ('WebseitennameUrlWahl', wagtail.core.blocks.URLBlock(help_text='Falls der Webseitenname auf keine Seite dieser Webseite verlinken soll, können sie hier eine Url eingeben z.B. roterkeil.net', required=False)), ('ExtraButton', wagtail.core.blocks.BooleanBlock(help_text='Hier können sie einen zusätzlichen Button ganz links in der Navigationsleiste hinzufügen.', required=False)), ('ExtraButtonTitel', wagtail.core.blocks.CharBlock(required=False)), ('ExtraButtonSeitenwahl', wagtail.core.blocks.PageChooserBlock(help_text='Hier kann eine Seite dieser Website ausgewählt werden', required=False)), ('ExtraButtonUrlWahl', wagtail.core.blocks.URLBlock(help_text='Hier kann eine Url eingegeben werden z.B. roterkeil.net', required=False)), ('Einstellungen', wagtail.core.blocks.StructBlock([('ExtraButtonFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die primär Farbe', required=False)), ('ExtraButtonStil', wagtail.core.blocks.ChoiceBlock(choices=[('RundeEcken', 'RundeEcken'), ('RundeEckenXl', 'RundeEckenXl'), ('KantenEcken', 'KantenEcken'), ('KantenEckenXl', 'KantenEckenXl')])), ('ExtraButtonUnausgefuellt', wagtail.core.blocks.BooleanBlock(help_text='Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat', required=False)), ('ExtraButtonSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß', required=False)), ('NavigationsleisteZentriert', wagtail.core.blocks.BooleanBlock(help_text='Wenn dieses Kästchen ausgewählt ist, werden alle Reiter in der Mitte der Navigationsleiste zentriert', required=False))], form_classname='structblock', help_text='Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.')), ('NavigationsleistenReiter', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('ReiterTitel', wagtail.core.blocks.CharBlock(required=True)), ('ReiterSeitenWahl', wagtail.core.blocks.PageChooserBlock(required=False)), ('ReiterUrlWahl', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False))])))])), ('MASTERHEAD', wagtail.core.blocks.StructBlock([('Titel', wagtail.core.blocks.CharBlock(required=True)), ('Unterstrich', wagtail.core.blocks.BooleanBlock(help_text='Fügt einen Kurzen Unterstrich als Designelement hinzu, der Titel und Untertitel optisch trennt', required=False)), ('Untertitel', wagtail.core.blocks.TextBlock(required=False)), ('Hintergrundbild', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Button', wagtail.core.blocks.BooleanBlock(required=False)), ('ButtonTitel', wagtail.core.blocks.CharBlock(required=False)), ('ButtonSeitenwahl', wagtail.core.blocks.PageChooserBlock(help_text='Hier kann eine Seite dieser Website ausgewählt werden', required=False)), ('ButtonUrlWahl', wagtail.core.blocks.URLBlock(help_text='Hier kann eine Url eingegeben werden z.B. roterkeil.net', required=False)), ('Einstellungen', wagtail.core.blocks.StructBlock([('HintergrundbildXPosition', wagtail.core.blocks.CharBlock(help_text='Ist das bild in Verschiedenen Browserfenstergrößen durchschnittlich zu weit unten(Kopf einer Person nicht sichtbar wenn er im Bild oben ist), kann man hier eine Zahl zwischen 0 und 100 eigeben. 0 würde dafür sorgen, dass das bild immer oben anfängt. Default=50', required=False)), ('HintergrundbildYPosition', wagtail.core.blocks.CharBlock(help_text='Ist das bild in Verschiedenen Browserfenstergrößen durchschnittlich zu weitnach rechts verrückt, kann man hier eine Zahl zwischen 0 und 100 eigeben. 0 würde dafür sorgen, dass das bild immer links anfängt.Default=50', required=False)), ('HintergrundbildGroesse', wagtail.core.blocks.ChoiceBlock(choices=[('sehrkleinP', 'sehrklein%'), ('kleinP', 'klein%'), ('grossP', 'gross%'), ('sehrkleinA', 'sehrkleinAbsolut'), ('kleinA', 'kleinAbsolut'), ('grossA', 'grossAbsolut')], help_text='sehrklein% entspricht etwa 20% der zu verfügung stehenden höhe.Klein etwa 30% Groß etwa 60%. SehrkleinAbsolut etwa 200px. KleinAbsolut etwa 380px. GroßAbsolut etwa 700px.', icon='cup', required=False)), ('HintergrundbildFixiert', wagtail.core.blocks.BooleanBlock(help_text='Fixiert das Hintergrund Bild, sodass es sich beim Scrollen nicht bewegt', required=False)), ('TitelAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('TitelSchriftgroesse', wagtail.core.blocks.CharBlock(help_text='fs- gefolgt von einer Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten z.B. fs-1', required=False)), ('UntertitelSchriftgroesse', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 6. 1 ist am Größten 6 am kleinsten', required=False)), ('UnterstrichAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('TitelSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Schwarz', required=False)), ('UntertitelSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist Schwarz', required=False)), ('UnterstrichSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f Voreingestellt ist die Primärfarbe', required=False)), ('InhaltHorizontaleAusrichtung', wagtail.core.blocks.ChoiceBlock(choices=[('a', 'linksseitig'), ('m', 'zentriert'), ('e', 'rechtseitig')], help_text='Wollen sie ihren Text linksbündig können sie hier z.B. linksseitig auswählen.', icon='cup', required=False)), ('ButtonFarbe', wagtail.core.blocks.CharBlock(help_text='Hier kann z.B. primary angegeben werden für ein Button in der Hauptfarbe der Website secundary succsess danger warning info light und dark sind weitere verfügbare Farben', required=False)), ('ButtonStil', wagtail.core.blocks.ChoiceBlock(choices=[('RundeEcken', 'RundeEcken'), ('RundeEckenXl', 'RundeEckenXl'), ('KantenEcken', 'KantenEcken'), ('KantenEckenXl', 'KantenEckenXl')])), ('ButtonUnausgefuellt', wagtail.core.blocks.BooleanBlock(help_text='Hier kann man einstellen, dass der Button keine Hintergrundfarbe hat', required=False)), ('ButtonSchriftFarbe', wagtail.core.blocks.CharBlock(help_text='In Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f. Voreingestellt ist Weiß', required=False)), ('ButtonAbstandOben', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10.Oder <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('Icon', wagtail.core.blocks.CharBlock(help_text='Hier wird ein Icon Oberhalb des Titels hinzugefügt. z.B. Ein Großer Haken in der Primärfarbe bi-check fs-1 text-primary Icons findet man auf https://icons.getbootstrap.com/ fs-1 bedeutet große Schrift fs-4 wäre kleiner. text-primary wäre die Hauptfarbe text-secundary die Zweitfarbe.', required=False))], form_classname='structblock', help_text='Optional. Klappt sich aus, wenn man mit dem Mauszeiger drüber fährt.'))])), ('GALLERIE', wagtail.core.blocks.StructBlock([('Image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image4', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image5', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image6', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image1Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image2Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image3Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image4Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image5Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image6Thumbnail', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Image1Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image1Project', wagtail.core.blocks.TextBlock(required=True)), ('Image2Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image2Project', wagtail.core.blocks.TextBlock(required=True)), ('Image3Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image3Project', wagtail.core.blocks.TextBlock(required=True)), ('Image4Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image4Project', wagtail.core.blocks.TextBlock(required=True)), ('Image5Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image5Project', wagtail.core.blocks.TextBlock(required=True)), ('Image6Categorie', wagtail.core.blocks.TextBlock(required=True)), ('Image6Project', wagtail.core.blocks.TextBlock(required=True))])), ('CONTACT', wagtail.core.blocks.StructBlock([('HEADER', wagtail.core.blocks.TextBlock(required=True)), ('headerSubtitle', wagtail.core.blocks.TextBlock(required=True)), ('button', wagtail.core.blocks.TextBlock(required=True)), ('HintergrundBild', wagtail.images.blocks.ImageChooserBlock(required=False)), ('AbstandNachObenUnten', wagtail.core.blocks.TextBlock(required=False)), ('HintergrundFarbe', wagtail.core.blocks.TextBlock(required=False)), ('SchriftFarbe', wagtail.core.blocks.TextBlock(required=False))])), ('VideoHeader', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('subtitle', wagtail.core.blocks.TextBlock(required=True)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('BUTTON', wagtail.core.blocks.TextBlock(required=False))])), ('CardPicture', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=True)), ('subtitle', wagtail.core.blocks.TextBlock(required=True)), ('btn', wagtail.core.blocks.TextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('position', wagtail.core.blocks.TextBlock(required=False)), ('rounded', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandNachUnten', wagtail.core.blocks.CharBlock(required=False)), ('AbstandNachOben', wagtail.core.blocks.CharBlock(required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])), ('ThreeImagesCallToAction', wagtail.core.blocks.StructBlock([('HintergrundFarbe', wagtail.core.blocks.TextBlock(required=True)), ('BackgroundImage', wagtail.images.blocks.ImageChooserBlock(required=False)), ('title1', wagtail.core.blocks.TextBlock(required=True)), ('title2', wagtail.core.blocks.TextBlock(required=True)), ('title3', wagtail.core.blocks.TextBlock(required=True)), ('subtitle1', wagtail.core.blocks.TextBlock(required=True)), ('subtitle2', wagtail.core.blocks.TextBlock(required=True)), ('subtitle3', wagtail.core.blocks.TextBlock(required=True)), ('info1', wagtail.core.blocks.TextBlock(required=True)), ('info2', wagtail.core.blocks.TextBlock(required=True)), ('info3', wagtail.core.blocks.TextBlock(required=True)), ('btn1', wagtail.core.blocks.TextBlock(required=False)), ('btn2', wagtail.core.blocks.TextBlock(required=False)), ('btn3', wagtail.core.blocks.TextBlock(required=False)), ('image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('CardBlock', wagtail.core.blocks.StructBlock([('Titel', wagtail.core.blocks.CharBlock(required=False)), ('TitelAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('UnterstrichAbstandUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('Unterstrich', wagtail.core.blocks.BooleanBlock(required=False)), ('id', wagtail.core.blocks.CharBlock(help_text='Wenn man von einer anderer Seite nicht nur diese seite aufrufen, sondern auch hier hin scrollen will, kann man www.<url>/#<id> verwenden', required=False)), ('AbstandNachObenUnten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('HintergrundFarbe', wagtail.core.blocks.CharBlock(help_text='Farbe in Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f', required=False)), ('HintergrundBild', wagtail.images.blocks.ImageChooserBlock(help_text='Setzt die Mindesthöhe auf 700px!', required=False)), ('SchriftFarbe', wagtail.core.blocks.CharBlock(help_text='Farbe in Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f', required=False)), ('rounded', wagtail.core.blocks.BooleanBlock(required=False)), ('CardOptic', wagtail.core.blocks.BooleanBlock(required=False)), ('Schatten', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandZwischenBildern', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('Breakpoint', wagtail.core.blocks.CharBlock(help_text='Bei welcher größe Umgebrochen wird Default sm', required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('RichText', wagtail.core.blocks.RichTextBlock(required=False)), ('AbstandSeitenText', wagtail.core.blocks.CharBlock(help_text='Zahl zwischen 1 und 10. <Breakpoint> - <Zahl> z.B. sm-1 oder xl-3 ist auch möglich. Breakpoints(sm,md,xl,lg,xxl) Dies führt dazu, dass der Abstand so lange gilt, bis der Breakpoint unterschritten wird. Default=0 ', required=False)), ('HintergrundFarbeKarte', wagtail.core.blocks.CharBlock(help_text='Farbe in Englisch z.B. gray oder white sonst in Hexcode z.b #12a23f', required=False)), ('icon', wagtail.core.blocks.CharBlock(help_text='Icons statt bilder', required=False)), ('ButtonKlein', wagtail.core.blocks.BooleanBlock(required=False)), ('ButtonPosition', wagtail.core.blocks.CharBlock(help_text='Relative Position des Buttons. a für am Anfang m für Zentriert und e für am Ende', required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('Buttontext', wagtail.core.blocks.TextBlock(required=False))])))])), ('SlideShow', wagtail.core.blocks.StructBlock([('image1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title1', wagtail.core.blocks.CharBlock(required=False)), ('title2', wagtail.core.blocks.CharBlock(required=False)), ('title3', wagtail.core.blocks.CharBlock(required=False)), ('info1', wagtail.core.blocks.TextBlock(required=False)), ('info2', wagtail.core.blocks.TextBlock(required=False)), ('info3', wagtail.core.blocks.TextBlock(required=False))])), ('ClickableCardBlock', wagtail.core.blocks.StructBlock([('AbstandNachObenUnten', wagtail.core.blocks.CharBlock(required=False)), ('HintergrundFarbe', wagtail.core.blocks.CharBlock(required=False)), ('SchriftFarbe', wagtail.core.blocks.CharBlock(required=False)), ('AbstandZwischenBildern', wagtail.core.blocks.BooleanBlock(required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('Klein', wagtail.core.blocks.BooleanBlock(required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('button_page', wagtail.core.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.core.blocks.URLBlock(help_text='If the button page above is selected, that will be used first.', required=False)), ('ButtonTitle', wagtail.core.blocks.TextBlock(required=False))])))])), ('Parralax', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('titleTop', wagtail.core.blocks.CharBlock(required=False)), ('titleLeft', wagtail.core.blocks.CharBlock(required=False)), ('AbstandNachObenUnten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('AbstandSeiten', wagtail.core.blocks.CharBlock(help_text='Default=0', required=False)), ('HintergrundFarbe', wagtail.core.blocks.CharBlock(required=False)), ('SchriftFarbe', wagtail.core.blocks.CharBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('ResponsiveGallery', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('Bild', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('ParallaxBild', wagtail.core.blocks.StructBlock([('HintergrundBild', wagtail.images.blocks.ImageChooserBlock(required=True)), ('Bildhoehe', wagtail.core.blocks.CharBlock(help_text='1-200. 100 wäre Quadratisch', required=True)), ('Bildverschiebung', wagtail.core.blocks.CharBlock(help_text='-20 - 20. Anfängliche Verschiebung des Bildes aus dem Zentrum raus', required=True))]))], blank=True, null=True),
        ),
    ]
