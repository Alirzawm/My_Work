import re
def validate_phone_number(تلفن_همراه):
    pattern = re.compile(r'^09\d{9}$')
    if re.match(pattern, تلفن_همراه):
        return True
    else:
        return False

تلفن_همراه = input("09030799574")

if validate_phone_number(تلفن_همراه):
    print("Correct")
else:
    print("False")