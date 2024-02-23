def readInt(msg, min=False, max=False, valid=False):
    '''
    This function only accepts integer numbers. It mostly works with closed
    options inside a list. It works this way if valid is set as False. If
    valid is set True, it works to validate the year choosen to create a
    new sheet.
    '''
    while True:
        try:
            n = int(input(msg))
            if n == 0:
                return False
            if valid:                   # In the function newSheet(), min and max values are set as
                if n < min or n > max:  # 1970 and actual year.
                        print('\033[31mERROR! Please, type a valid year.\033[m')
                else:
                    return str(n)
            else:
                if min or max:  # Only if you want to set min or max values for your entry.
                    if n < min or n > max:
                        print('\033[31mERROR! Please, type a valid value from the list above.\033[m')
                    else:
                        return n
                else:
                    return n
        
        except (ValueError, TypeError):
            print('\033[31mERROR! Please, type a valid INTEGER number.\033[m')

        except KeyboardInterrupt:
            print()
            return 8


def readMoney(txt):
    '''
    Only read values that is possible to be recognized as monetary. Accepts:
    1; 1.0; 1.00; 1,0; 1,00. If number is integer, becomes a floating-point
    number with two decimal places anyway. At the end of the process, replaces
    the dot for a comma (like a real monetary value).
    '''
    while True:

        try:
            entry = input(txt).strip()

            if '.' in entry:
                if len(entry) - 1 - entry.find('.') == 2:   # If entry is a floating-point number
                    conversion = entry.replace(".", "", 1)  # with two decimal places. Replaces dot
                    if conversion.isnumeric():              # one time only.
                        result = int(conversion) / 100
                    
                elif len(entry) - 1 - entry.find('.') == 1: # If entry is a floating-point number
                    conversion = entry.replace(".", "", 1)  # with one decimal place (1.1 is 1 dollar
                    if conversion.isnumeric():              # and 10 cents).
                        result = int(conversion) / 10
                    
            if ',' in entry:
                if len(entry) - 1 - entry.find(',') == 2:   # Same thing as above, but if user preferred
                    conversion = entry.replace(",", "", 1)  # to directly use a comma.
                    if conversion.isnumeric():
                        result = int(conversion) / 100
                    
                elif len(entry) - 1 - entry.find(',') == 1:
                    conversion = entry.replace(",", "", 1)
                    if conversion.isnumeric():
                        result = int(conversion) / 10
                    
            if entry.isnumeric():
                result = int(entry)
            
            if len(str(float(result))) <= 14:
                return str(f'${result:.2f}').replace('.', ',')
            else:
                print(f'\033[31mERROR! Entry must have a max legth of 14!\033[m')
            
            print(f'\033[31mERROR! "{entry}" is an invalid value!\033[m')
        except Exception:
            print(f'\033[31mERROR! Something is wrong with your amount entry.\nPlease, enter a valid value.\033[m')


def readDate(txt, file):
    '''
    This function reads the day, month and year of a typed date, and if the date is valid
    and corresponding to the present sheet when registering an income or expense.
    '''
    from files import months30, months31
    while True:
        conditions = False
        
        while not conditions:
        
            try:
                entry = input(txt).strip()
                month = int(entry[0:2])
                day = int(entry[3:5])
                year = int(entry[6:10])
            

                if len(entry) != 10:
                    print('\033[31mERROR! Invalid date entry.\033[m')
                    break

                elif int(file[0:4]) != year:
                    print('\033[31mERROR! Invalid year for this sheet.\033[m')
                    break
                
                elif int(file[5:7]) != month:
                    print('\033[31mERROR! Invalid month for the year of this sheet.\033[m')
                    break
                
                elif day < 1:
                    print('\033[31mERROR! Invalid day entry.\033[m')
                    break

                elif month in months30 and day > 30:
                    print('\033[31mERROR! Invalid day for the month of this sheet.\033[m')
                    break
                
                elif month in months31 and day > 31:
                    print('\033[31mERROR! Invalid day for the month of this sheet.\033[m')
                    break
                
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # Checks if year is a leap year.
                    if month == 2 and day > 29:
                        print('\033[31mERROR! Invalid day for the month of this sheet.\033[m')
                        break
                else:
                    if month == 2 and day > 28:
                        print('\033[31mERROR! Invalid day for the month of this sheet.\033[m')
                        break

            except Exception:
                print(f'\033[31mERROR! Something is wrong with your date entry.\nPlease, enter a valid date format.\033[m]')
                break

            return entry


def entryValid(txt, length=60):
    '''
    Only validates the length of an str entry.
    '''
    while True:
        entry = input(txt)
        if len(entry) > length:
            print(f'\033[31mYour entry must have a max limit of {length} characters!\033[m')
        else:
            return entry


def monthValid(txt, min=1, max=12):
    '''
    Validates the month in the process of creating
    a new sheet.
    '''
    from files import months
    while True:
        entry = readInt(txt)
        if entry == 0:
            return False
        if entry < min or entry > max:
            print(f'\033[31mPlease enter a valid month value!\033[m')
        else:
            for k in months.keys():
                if entry == k:
                    if len(str(k)) == 1:
                        k = str(f'0{k}')
                    return k
