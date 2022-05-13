import PyPDF2

with open('test.txt') as f:
    pdf = PyPDF2.PdfFileReader(f)
