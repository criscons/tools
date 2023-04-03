#pip3 install reportlab
from  reportlab.pdfgen import canvas

#create a new file pdf
pdf_file =canvas.Canvas("example1.pdf")

#add text to the PDF file
pdf_file.drawString(72,720,"Hello world")
pdf_file.drawString(72,700,"Document")
pdf_file.drawString(72,680,"PDF")
pdf_file.drawString(72,660,"Files")
pdf_file.drawString(72,640,"Bye bye")

pdf_file.save()

print("Created!")
