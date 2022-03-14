import sys
import os
from pdfrw import PdfReader, PdfWriter, PageMerge

def splitpage(src):
    for y_pos in (0, 0.5):
        page = PageMerge()
        page.add(src, viewrect=(0, y_pos, 1, 0.5))
        page[0].y = page[0].h/15
        yield page.render()

if(len(sys.argv)>1):
    inpfn = sys.argv[1]
else:
    print("Inserisci nome completo file: ")
    inpfn=input()

print("splitting ..... ", inpfn)
outfn = 'splitv.' + os.path.basename(inpfn)
writer = PdfWriter()
for page in PdfReader(inpfn).pages:
    writer.addpages(splitpage(page))
writer.write(outfn)