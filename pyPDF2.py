import PyPDF2

def compress_pdf(input_pdf, output_pdf):
    pdf_writer = PyPDF2.PdfWriter()
    pdf_reader = PyPDF2.PdfReader(input_pdf)

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.compressContentStreams()  # This compresses the content of the page
        pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

input_pdf = 'input.pdf'
output_pdf = 'compressed_output.pdf'
compress_pdf(input_pdf, output_pdf)
