#pip3 install pdf2docx
from pdf2docx import Converter

filepdf = 'namefile.pdf'
filedocx = 'namefile.docx'

conv = Converter(filepdf)
conv.convert(filedocx)

conv.close()
