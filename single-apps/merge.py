import PyPDF2
from os import listdir
from PyPDF2 import merger

from PyPDF2.pdf import PdfFileReader

listafile = listdir()

listafile.sort()
nomeDest = input()
pdfDest = open(nomeDest, "wb")
pdfMerger = PyPDF2.PdfFileMerger()

for nomeFile in listafile:
    if nomeFile.endswith(".pdf"):
        print(nomeFile)
        
        pdfFile = open(nomeFile, "rb")
        readerPdf = PyPDF2.PdfFileReader(pdfFile)
        pdfMerger.append(readerPdf)
        pdfFile.close()
        
    
pdfMerger.write(pdfDest)
pdfDest.close()