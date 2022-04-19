from simple_term_menu import TerminalMenu
from PyPDF2.pdf import PdfFileReader
from PyPDF2.pdf import PdfFileWriter
from PyPDF2 import PdfFileMerger
from os import listdir
from os.path import exists

def merge():
    work_dir = get_work_dir()
    dest_name = get_file_name_path(work_dir, "merged")
    pdf_merger = PdfFileMerger()
    print("merging... ", end='')
    for file in get_file_list(work_dir):
        if file.endswith(".pdf"):
            temp_file = open(work_dir+file, "rb")
            pdf_reader = PdfFileReader(temp_file, strict=False)
            pdf_merger.append(pdf_reader)
            temp_file.close()
    
    pdf_dest = open(dest_name, "wb")
    pdf_merger.write(pdf_dest)
    pdf_dest.close()
    

def rotate():
    work_file_name = False
    while not work_file_name:
        work_dir = get_work_dir()
        work_file_name = get_file_name(work_dir)
    dest_name = get_file_name_path(work_dir, "rotated")
    opt = ["90° orario", "90° antiorario", "180 gradi"]
    menu = TerminalMenu(opt, title="scegliere il senso di rotazione.")
    val = menu.show()

    input_file = open(work_file_name, "rb")
    reader = PdfFileReader(input_file)
    writer = PdfFileWriter()
    match val:
        case 0:
            for i in range(0, int(reader.getNumPages())):
                pageI = reader.getPage(i)
                pageI.rotateCounterClockwise(-90)
                writer.addPage(pageI)
        case 1:
            for i in range(0, int(reader.getNumPages())):
                pageI = reader.getPage(i)
                pageI.rotateCounterClockwise(90)
                writer.addPage(pageI)
        case 2:
            for i in range(0, int(reader.getNumPages())):
                pageI = reader.getPage(i)
                pageI.rotateCounterClockwise(180)
                writer.addPage(pageI)

    outputFile = open(dest_name, "wb")
    writer.write(outputFile)
    input_file.close()
    outputFile.close()


def vertical_split():
    print("splitting...")


def get_file_list(dir):
    file_list = listdir(dir)
    file_list.sort()
    return file_list

def get_work_dir():
    work_dir = input("Inserisci cartella contenente i file:")
    if not work_dir.endswith("/"):
        work_dir = work_dir+"/"
    return work_dir

def get_file_name_path(dir, label):
    opt = ["Yes", "No"]
    menu = TerminalMenu(opt, title="Salvare il documento nella cartella dei file?")
    val = menu.show()
    dest_name = input("Inserisci nome file di destinazione:")
    if not dest_name.endswith(".pdf"):
        if not dest_name:
            dest_name = dest_name+label+".pdf"
        else:
            dest_name = dest_name+".pdf"            
    if(val == 0):
        dest_name = dir + dest_name

    return dest_name
    
def get_file_name(dir):
    file_name = input("Inserisci nome file: ")
    if not file_name.endswith(".pdf"):
        file_name = file_name+".pdf"
    file_absolute_path = dir + file_name
    if not exists(file_absolute_path):
        return False
    else:
        return file_absolute_path
    