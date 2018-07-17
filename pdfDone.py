from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
 
def PDFMake(fileName,text):
    doc = SimpleDocTemplate(fileName+".pdf",
                            pagesize=letter,
                            rightMargin=72,
                            leftMargin=72,
                            topMargin=72,
                            bottomMargin=18)
    styles = getSampleStyleSheet()
 
    flowables = []
    para = Paragraph(text, style=styles["Normal"])
    flowables.append(para)
 
    doc.build(flowables)
 


