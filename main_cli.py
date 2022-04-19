from simple_term_menu import TerminalMenu
from utility import utility

def matcher(index):
    match index:
        case 0:
            return utility.rotate()
        case 1:
            return utility.merge()
        case 2:
            return utility.vertical_split()
        

def main():
    options = ["Rotate PDF", "Merge Multiple PDF", "Split vertical"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    matcher(menu_entry_index)

  

if __name__ == "__main__":
    main()