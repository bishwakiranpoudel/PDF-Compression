from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

def compress_pdf(input_pdf, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)

    with open(input_pdf, 'rb') as pdf_file:
        c.drawImage(ImageReader(pdf_file), 0, 0, width=letter[0], height=letter[1])

    c.save()

input_pdf = 'input.pdf'
output_pdf = 'compressed_output.pdf'
compress_pdf(input_pdf, output_pdf)
