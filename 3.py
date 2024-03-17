def validate_shamsi_date(date):
    try:
        day, month, year = map(int, date.split('/'))
        if day < 1 or day > 31:
            return False
        if month < 1 or month > 12:
            return False
        if year < 1:
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            if day > 31:
                return False
        elif month in [4, 6, 9, 11]:
            if day > 30:
                return False
        else:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        return True
    except ValueError:
        return False
date_input = input("1383/01/04")
if validate_shamsi_date(date_input):
    print("Correct")
else:
    print("False")