import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch

from reportlab.pdfgen import canvas
# from reportlab.
from reportlab.platypus import Table ,TableStyle,SimpleDocTemplate

buffer = io.BytesIO()

# Create the PDF object, using the buffer as its "file."
p = canvas.Canvas("hello.pdf")

# Draw things on the PDF. Here's where the PDF generation happens.
# See the ReportLab documentation for the full list of functionality.
p.drawString(0, 100, "StudioStreet Invoice")
p.drawString(300, 800,"Customer Name: Aditya Singh Chauhan")
p.drawString(300, 785,"Customer Email: aditya.juet@gmail.com")
p.drawString(0, 800,"Invoice Generation Date: 10th Oct 2020")
doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
elements = []
data= [['00', '01', '02', '03', '04'],
 ['10', '11', '12', '13', '14'],
 ['20', '21', '22', '23', '24'],
 ['30', '31', '32', '33', '34']]
t=Table(data)
t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
 ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))

elements.append(t)
elements.append(p)

doc.build(elements)






# Close the PDF object cleanly, and we're done.
# p.showPage()
p.save()