import PyPDF2

with open('sample.pdf', 'rb') as f:
    # read pdf file with PyPDF2
    pdf = PyPDF2.PdfFileReader(f)
    # get number of pages
    num_pages = pdf.getNumPages()
    # loop through pages
    for i in range(num_pages):
        # get page
        page = pdf.getPage(i)
        # get page content
        print(page.extractText())
        # get page size
        print(page.mediaBox)
        pdf_writer = PyPDF2.PdfFileWriter()
        pdf_writer.addPage(page)
    with open('sample.pdf', 'wb') as new_file:
        # write pdf file with PyPDF2
        pdf_writer.write(f)
