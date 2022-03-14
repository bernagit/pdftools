import sys
import os
from pdfrw import PdfReader, PdfWriter, PageMerge


def splitpage(src):
    '''Split a page into two (top and bottom)'''
    for y_pos in (0, 0.5):
        #print(y_pos)
        page = PageMerge()
        page.add(src, viewrect=(0, y_pos, 1, 0.5))
        page[0].y = page[0].h/15
        yield page.render()

inpfn = sys.argv[1]
print("splitting ..... ", inpfn)
outfn = 'splitv.' + os.path.basename(inpfn)
writer = PdfWriter()
for page in PdfReader(inpfn).pages:
    writer.addpages(splitpage(page))
writer.write(outfn)