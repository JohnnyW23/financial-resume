def lin(len=30):
    print('~' * len)


def title(txt, len=30, color=0, title=True):
    from time import sleep

    print()
    lin(len)
    if title:
        print(f'\033[{color}m{str(txt.strip().upper()).center(len)}\033[m')
    else:
        print(f'\033[{color}m{str(txt.strip()).center(len)}\033[m')
    lin(len)
    sleep(1)


def appMenu(list, len=30, color=0, index=0, listed=0):
    from time import sleep
    from readers import readInt

    sleep(1)
    title('MY FINANCIAL 1.0v', len, color, title=False)
    c = 1
    
    for item in list:
        print(f'[\033[{index}m{c}\033[m] – \033[{listed}m{item}\033[m')
        c += 1
        
    lin(len)

    while True:
        opc = readInt(f'\033[{index}mOption: \033[m', 1, 8)
        if not opc:
            print('\033[31mERROR! Please, type a valid value from the list above.\033[m')
        else:
            return opc


def sheetsMenu(length=30, color=0, index=0, inc=False, exp=False):
    import os
    from files import months
    from readers import readInt

    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    text_files = [file for file in files if file.endswith('.txt')]

    if len(text_files) == 0:
        print('\033[33m<There are no sheets. Create a sheet via app Menu (Option 1)>\033[m')
    else:
        print('\033[33mSheets available:\033[m')
        c = 1
        for file in text_files:
            for k, v in months.items():
                if k == int(file[5:7]) * 1:
                    month = v
                    year = file[0:4]
                    interface_name = f'{month} {year}'
                    print(f'[\033[{index}m{c}\033[m] - {interface_name}')
                    c += 1
        lin(length)
        opc = readInt(f'[0] to Cancel\n\033[{index}mOption: \033[m', 0, len(text_files))
        if not opc:
            return False, False
        else:
            target = f'{text_files[opc - 1]}'
            for k, v in months.items():
                if k == int(target[5:7]) * 1:
                    month = v
                    year = target[0:4]
                    interface_name = f'{month} {year}'
                    if inc:
                        title(f'+ {interface_name} +', length, color)
                    elif exp:
                        title(f'- {interface_name} -', length, color)
                    else:
                        title(f'{interface_name}', length, color)
            return text_files[opc - 1], interface_name
    

def instructions(len=30, color=0):
    from time import sleep

    title('Instructions', len, color)
    print('\033[33m', end='')
    print('WELCOME TO THE "MY FINANCIAL v1.0"!'.center(100))
    print('\033[m', end='')
    print('''
Created by: \033[36mDavi Nascimento\033[m
            February 2024
''')
    
    sleep(0.5)

    print('''->  The user must choose an option from the menu
    to execute one of the commands below.
''')

    sleep(0.5)
    ##############################################
    print('''1 - ADD NEW SHEET:
    User creates a new sheet based on desired year
    and month of register. If sheet already exists,
    it won't duplicate, the new sheet won't be
    created and the previus wheet won't be
    subscribed.
''')

    sleep(0.5)
    
    print('''2 - VIEW FINANCIAL RESUME:
    User chooses one of the existing sheets and the
    program shows a resume of it.
''')

    sleep(0.5)
    
    print('''3 - ADD INCOME:
    User adds an income to the corresponding entry.
    Will obviously always count as a positive value.
    Entry has a limit of characters length, a date
    validator and a monetary value validator.
''')

    sleep(0.5)
    
    print('''4 - ADD EXPENSE:
    User adds an expense to the corresponding entry.
    Will obviously always count as a negative value.
    Entry has a limit of characters length, a date
    validator and a monetary value validator.
''')

    sleep(0.5)
    
    print('''5 - DELETE ENTRY:
    User has the option to delete a single entry from
    the corresponding sheet.
''')

    sleep(0.5)
    
    print('''6 - DELETE SHEET:
    User has the opyion to delete the entire sheet.
''')

    sleep(0.5)
    
    print('''7 - INSTRUCTIONS:
    Displays the current menu with instructions
    about all the commands in the application.
''')

    sleep(0.5)
    
    print('''8 - EXIT PROGRAM:
    Exits the application and shuts down the
    program.''')


def exit(len=30, color=0):
    from time import sleep

    title('Exiting program...', len, color)
    sleep(1)
    print('\033[36mThank you and come back!\033[m')
    print()
