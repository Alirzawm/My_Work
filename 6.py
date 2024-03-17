def check_valid_city(Khorramabad):
    valid_counties = ["Tehran", "Mashhad", "Esfahan", "Shiraz","Khorramabad"]
    if Khorramabad in valid_counties:
        return True
    else:
        return False

birth_county = input("Iran")
if check_valid_city(birth_county):
    print("Correct")
else:
    print("False")