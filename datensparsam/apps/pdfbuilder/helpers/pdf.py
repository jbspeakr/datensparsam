from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch


class Pdf(object):

    __story = []
    __styles = getSampleStyleSheet()
    __doc = None

    def __init__(self, buff):
        self.__doc = SimpleDocTemplate(
            buff,
            pagesize=letter,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18)

    def add_address(self, address):
        for part in address:
            ptext = '<font size=12>%s</font>' % part.strip()
            self.__story.append(Paragraph(ptext, self.__styles["Normal"]))
        self.add_spacer(24)

    def add_spacer(self, height):
        self.__story.append(Spacer(1, height))

    def add_heading(self, heading):
        self.add_spacer(48)
        self.__story.append(Paragraph(heading, self.__styles["Heading1"]))
        self.add_spacer(24)

    def add_paragraph(self, paragraph):
        if paragraph:
            self.__story.append(Paragraph(paragraph, self.__styles["Normal"]))
            self.add_spacer(12)
        else:
            pass

    def make(self):
        self.__doc.build(self.__story)
