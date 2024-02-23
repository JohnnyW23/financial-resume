months = {1:'January', 2:'February', 3:'March', 4:'April',
          5:'May', 6:'June', 7:'July', 8:'August',
          9:'September', 10:'October', 11:'November', 12:'December'}

months31 = [1, 3, 5, 7, 8, 10, 12]
months30 = [4, 6, 9, 11]

def newSheet():
    from readers import monthValid, readInt
    from datetime import datetime
    
    for k, v in months.items():
        print(f'\033[35m{k}\033[m – {v}')
    print()
    month = monthValid('[0] to cancel\nChoose your month: ')
    if not month:
        return False
    year = readInt('Type the year: ', 1970, datetime.today().year, True)
    if not year:
        return False
    name = f'{year}_{month}.txt'
    return name


def fileExists(name):
    '''
    This function examines if file (name) exists. If it does, it won't create
    another sheet corresponding to the desired month and year and, instead,
    displays a message about the sheet already existing. Otherwise, it calls
    the function fileCreate(name).
    '''
    try:
        with open(name, 'rt'):
            print('This sheet already exists!')
        
    except FileNotFoundError:
        fileCreate(name)


def fileCreate(name):
    '''
    Creates the choosen sheet in the funcion newSheet(). Then, displays a
    message for the user that the sheet was created. This function
    translates the text file name to the corresponding names of month and
    year.
    '''
    try:
        a = open(name, 'wt+')
        a.close()
        
    except FileNotFoundError:
        print('\033[31mERROR: Could not create new file: FileNotFoundError.\033[m')

    except IOError:
        print('\033[31mERROR: Could not create new file: IOError.\033[m')

    else:
        month = name[5:7]
        year = name[0:4]
        for k, v in months.items():
            if k == int(month) * 1:  # Everytime you see "interface_name", in means it's the
                month = v  # text file name translated to a way the user easily understands.
                break  # For example: 2023_04.txt becomes "April 2023"
        interface_name = f'{month} {year}'
        print(f'\033[37mSheet \033[33m{interface_name}\033[37m created with success!\033[m')


def fileLineRead(name, line):
    '''
    Created to work with fileRead(name, interface_name) and to allow the
    function to work properly by reading a file line.
    '''
    with open(name, 'r') as file:
        for i, l in enumerate(file, 1):
            if i == line:
                return l


def fileRead(name, interface_name):
    '''
    Displays a sheet content. If it's empty, it warns the user about it. Oherwise,
    colors the sheet's incomes with green, sheet's expenses with red and sheet's
    "Total" sections depending if it's positive or negative.
    '''
    from os.path import getsize

    try:
        a = open(name, 'rt')

    except:
        print('\033[31mERROR: Could not read file.\033[m')

    else:
        if getsize(name) == 0:
            print(f'\033[32m<No entrys registered in \033[33m"{interface_name}"\033[32m>\033[m')

        else:
            lines = len(a.readlines())

            for l in range(1, lines + 1):
                entry = fileLineRead(name, l)
                positive = entry.find('POSITIVE', 68)  # The result is written starting at column 68. The .find() method must be used
                negative = entry.find('NEGATIVE', 68)  # starting at this point because what if the name of the event contains
                if entry[0] == 'I' or positive != -1:  # the words "positive" or "negative", no matter how many times?
                    print(f'{l:^3} - \033[32m{entry}\033[m', end='')
                elif entry[0] == 'E' or negative != -1:
                    print(f'{l:^3} - \033[31m{entry}\033[m', end='')
                else:
                    print(f'{l:^3} -')

    finally:
        a.close()


def incomeEntry(file, interface_name):
    from readers import entryValid, readMoney, readDate

    event = entryValid('Type the event: ', 55).upper().strip()
    amount = readMoney('Type the amount value: ')
    date = readDate('Date [mm/dd/yyyy]: ', file)
    register = f'INCOME  | {event:<55} |{date}|{amount:>14}'
    totalErase(file)
    fileRegister(file, interface_name, register)
    totalizer(file)

'''
Whenever a entry is created, three process occurs after that:
totalerase(file) -> Erases the total section.
fileRegister(file, interface_name, register) -> Register a new line in the sheet
with all the info required.
totalizer(file) -> Creates a result based on the values of the entries, and prints
the result two lines under.
'''

def expenseEntry(file, interface_name):
    from readers import entryValid, readMoney, readDate

    event = entryValid('Type the event: ', 55).upper().strip()
    amount = readMoney('Type the amount value: ')
    date = readDate('Date [mm/dd/yyyy]: ', file)
    register = f'EXPENSE | {event:<55} |{date}|{amount:>14}'
    totalErase(file)
    fileRegister(file, interface_name, register, plus=False)
    totalizer(file)


def totalErase(name):
    from os.path import getsize

    with open(name, 'r+'):
        if getsize(name) > 0:
            lineDelete(name, 0)
            lineDelete(name, 0)


def lineDelete(name, choice):
    try:
        with open(name, 'r+') as file:
            lines = file.readlines()
            info = lines[choice - 1]
            del lines[choice - 1]
            file.seek(0)
            file.truncate()
            file.writelines(lines)

            return info

    except FileNotFoundError:
        print(f'\033[31mFile "{name}" not found.\033[m')


def fileRegister(name, interface_name, register, plus=True):
    try:
        a = open(name, 'at')
        
    except:
        print('\033[31mERROR: Could not open file.\033[m')
        
    else:
        try:
            a.write(f'{register}\n')
            
        except:
            print('There was an ERROR in data register.')
            
        else:
            if plus:  # plus simply checks if function is used to register an income or an expense
                print(f'\033[32mIncome added in sheet \033[m{interface_name}\033[32m!\033[m')
            else:
                print(f'\033[32mExpense added in sheet \033[m{interface_name}\033[32m!\033[m')
            a.close()


def totalizer(name):
    with open(name, 'r') as a:
        lines = a.readlines()

        positive = 0
        negative = 0

        for l in lines:
            value = int((l[(l.find('$')) + 1:]).replace(',', ''))
            value = value / 100

            if l[0:3] == 'INC':
                positive += value
            else:
                value *= -1
                negative += value
        result = positive + negative
        
        if result < 0:
            situation = 'NEGATIVE'
        else:
            situation = 'POSITIVE'
        
        result = f'${result:.2f}'
        
        with open(name, 'a') as a:
            register = f'TOTAL   |' + (' ' * 57) + f'| {situation} |' + f'{result:>14}'.replace('.', ',')
            a.write(f'\n{register}')


def entryDelete(name, interface_name):
    from readers import readInt
    from os.path import getsize

    with open(name, 'r+') as a:
        lines = a.readlines()

        if getsize(name) == 0:
            print(f'There are no entries to delete (\033[33m"{name}"\033[m is empty)')

        else:
            while True:
                try:
                    choice = readInt(f'Which entry do you want to delete from \033[33m"{interface_name}"\033[m?\n[0] to interrupt\n')
                    
                    if choice == 0:
                        print('\033[33mOperation interrupted!\033[m')
                        break

                    elif choice == len(lines) or choice == len(lines) - 1:
                        print("\033[31mYou can't erase this line!\033[m")

                    elif 1 <= choice <= len(lines) - 2:
                        info = lineDelete(name, choice)  # Here, the line is deleted, then the total section
                        totalErase(name)                 # is erased as well, because the value inside the entry
                        totalizer(name)                  # was deleted, so we need a new total, created with totalizer(name).
                        entry = info[9:66].strip().capitalize()
                        situation = info[0:7].strip().lower()
                        value = info[78:92].strip()
                        print(f'Your {situation} with value {value} \033[33m({entry})\033[m was deleted with success!')
                        break

                    else:
                        print('\033[31mChoose a valid option!\033[m')
                        
                except IndexError:
                    print('\033[31mChoose a valid task index.\033[m')


def fileDelete(name, interface_name):
    from os import remove

    while True:
        answer = input(f'Are you sure you want to delete your sheet "{interface_name}"? [Y/N]: ').upper().strip()
        if answer == 'N':
            print('\033[33mOperation interrupted!\033[m')
            break

        elif answer == 'Y':
            remove(name)
            print(f'Your sheet \033[33m{interface_name}\033[m was deleted with success!')
            break

        else:
            print('\033[31mERROR! Enter a valid entry (Y or N).\033[m')
        