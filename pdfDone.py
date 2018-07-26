from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
 
def PDFMake(fileName,text):
    font_file = 'C:\Windows\Fonts\kalpurush.ttf'
    symbola_font = TTFont('Bangla', font_file)
    pdfmetrics.registerFont(symbola_font)
    
    
    doc = SimpleDocTemplate(fileName,
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=18
                            )
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='TestStyle',
                               fontName='Bangla',
                               fontSize=12,
                               leading=12))
    

 
    flowables = []
    para = Paragraph(text, style=styles["TestStyle"])
    
    
    flowables.append(para)
 
    doc.build(flowables)

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)


 


