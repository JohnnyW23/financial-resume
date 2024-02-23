from layout import appMenu, title, sheetsMenu, instructions, exit
from time import sleep
from files import newSheet, fileExists, fileRead, incomeEntry, expenseEntry, entryDelete, fileDelete

print('''
Welcome to the app!''')

sleep(1)

menu = ['Add new sheet', 'View financial resume', 'Add income',
'Add expense', 'Delete entry', 'Delete sheet',
'Instructions', 'Exit program']

while True:
    option = appMenu(menu, 100, 36, 35, listed=0)

    if option == 1:
        title(menu[0], 100, 33)
        name = newSheet()
        if not name:
            print('\033[33mOperation interrupted!\033[m')
        else:
            fileExists(name)
            sleep(1)
    
    elif option == 2:
        title(menu[1], 100, 33)
        file, interface_name = sheetsMenu(100, 33, 36)
        if not file and not interface_name:
            print('\033[33mOperation interrupted!\033[m')
        else:
            fileRead(file, interface_name)
    
    elif option == 3:
        title(menu[2], 100, 33)
        file, interface_name = sheetsMenu(100, 32, 32, inc=True)
        if not file and not interface_name:
            print('\033[33mOperation interrupted!\033[m')
        else:
            incomeEntry(file, interface_name)

    elif option == 4:
        title(menu[3], 100, 33)
        file, interface_name = sheetsMenu(100, 31, 31, exp=True)
        if not file and not interface_name:
            print('\033[33mOperation interrupted!\033[m')
        else:
            expenseEntry(file, interface_name)
    
    elif option == 5:
        title(menu[4], 100, 33)
        file, interface_name = sheetsMenu(100, 34, 36)
        if not file and not interface_name:
            print('\033[33mOperation interrupted!\033[m')
        else:
            entryDelete(file, interface_name)
    
    elif option == 6:
        title(menu[5], 100, 33)
        file, interface_name = sheetsMenu(100, 34, 36)
        if not file and not interface_name:
            print('\033[33mOperation interrupted!\033[m')
        else:
            fileDelete(file, interface_name)
            
    elif option == 7:
        instructions(100, 33)

    else:
        exit(100, 33)
        break
