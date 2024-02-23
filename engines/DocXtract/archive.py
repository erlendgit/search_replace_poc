import zipfile
import xml.etree.ElementTree as ET


class Archive:
    """
    Hier onderzoek ik waar je tegen aan kan lopen als je tekst in een
    word document wilt aanpassen. Ik neem ook mee of ik bij de embedded excel
    bestanden kan komen.

    Bevindingen:
    - De tekst is versnipperd. Je moet eerst de snippers bij elkaar zoeken
    - Zelfs de start-sequence kan versnipperd zijn.
    - Excel bestanden zitten in de zip die zich .docx noemt.

    Voorlopige conclusie:
    - Als het kan beperk ik me tot het vervangen van de teksten met de bestaande tool.
    - Aanpassen van Excel bestanden vraagt verder onderzoek.

    """
    def __init__(self, path):
        self.path = path
        self.zipfile = zipfile.ZipFile(path)

    def list_contents(self):
        logger = Printer()
        with self.zipfile.open("word/document.xml") as f:
            tree = ET.parse(f)
            root = tree.getroot()
            # logger.force(root.tag)
            for child in root:
                # logger.force("=> " + root.tag)
                for paragraph in child:
                    # logger.force("=> => " + paragraph.tag)
                    for region in paragraph:
                        # logger.force("=> => => " + region.tag)
                        for element in region:
                            logger.force("=> => => => " + element.tag)
                            logger.maybe_start(element)
                            logger.maybe_track(element)
                            logger.maybe_stop(element)


class Printer:
    def __init__(self):
        self.is_open = False
        self.starting_element = None
        self.in_between_elements = None

    def start_writing(self, element):
        self.starting_element = element
        self.in_between_elements = []
        self.is_open = True

    def maybe_start(self, element):
        if element.text and '{{' in element.text:
            print("Starting...")
            self.start_writing(element)

    def maybe_stop(self, element):
        if element.text and '}}' in element.text:
            print("Stopping...")
            self.stop_writing()

    def maybe_track(self, element):
        if not self.is_open or element is self.starting_element:
            return
        self.in_between_elements.append(element)
        print("Processing {} {}".format(element.tag, element.text))
        if element.text:
            self.starting_element.text = self.starting_element.text + element.text
            print("=> => => => => " + element.text)

    def stop_writing(self):
        if not self.is_open:
            return
        for element in self.in_between_elements:
            del(element)
        self.is_open = False

    def info(self, text):
        if self.is_open and text:
            print("{(=" + text + "=)}")

    def force(self, *args):
        print(*args)
