import sys
from os import listdir
from pdfrw import PdfReader, PdfWriter, PageMerge

def splitpage(src):
    for y_pos in (0, 0.5):
        page = PageMerge()
        page.add(src, viewrect=(0, y_pos, 1, 0.5))
        page[0].y = page[0].h/15
        yield page.render()

listafile = listdir()
listafile.sort()

for nomeFile in listafile:
    if nomeFile.endswith(".pdf"):
        writer = PdfWriter()
        print("Splitting... ", nomeFile)
        for page in PdfReader(nomeFile).pages:
            nomenuovo='split_'+nomeFile
            writer.addpages(splitpage(page))
        writer.write(nomenuovo)