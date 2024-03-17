import re
def validate_phone_number(تلفن_ثابت):
    pattern = r'^0[1-9]\d{9}$'

    if re.match(pattern, تلفن_ثابت):
        return True
    else:
        return False

تلفن_ثابت = input("066_33332211")
if validate_phone_number(تلفن_ثابت):
    print("Correct")
else:
    print("False")