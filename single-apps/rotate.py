from PyPDF2.pdf import PdfFileWriter
from PyPDF2.pdf import PdfFileReader
from PyPDF2.pdf import PageObject

writer = PdfFileWriter()
inputFile = open("file1", "rb")
outputFile = open("fileout", "wb")
reader = PdfFileReader(inputFile)

#rotate pdf 
for i in range(0, int(reader.getNumPages())):
    pageI = reader.getPage(i)
    pageI.rotateCounterClockwise(90)
    writer.addPage(pageI)

writer.write(outputFile)
