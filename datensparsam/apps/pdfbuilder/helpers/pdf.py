from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


class SimplePdf(object):
    ''' Provides functionality to create simple PDF documents '''
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
        self._add_spacer(24)

    def add_heading(self, heading):
        self._add_spacer(48)
        self.__story.append(Paragraph(heading, self.__styles["Heading1"]))
        self._add_spacer(24)

    def add_bulleted_paragraph(self, paragraph):
        if paragraph:
            self._add_spacer(12)
            self.__story.append(Paragraph(paragraph, self.__styles["Normal"], bulletText='-'))
        else:
            pass

    def add_paragraph(self, paragraph, spacer):
        if paragraph:
            self._add_spacer(spacer)
            self.__story.append(Paragraph(paragraph, self.__styles["Normal"]))
        else:
            pass

    def make(self):
        self.__doc.build(self.__story)

    def _add_spacer(self, height):
        self.__story.append(Spacer(1, height))
