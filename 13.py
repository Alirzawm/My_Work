def check_marital_status(وضعیت):
    if وضعیت.lower() == 'مجرد' or وضعیت.lower() == 'متاهل':
        return True
    else:
        return False

وضعیت_تاهل = input("مجرد")
if check_marital_status(وضعیت_تاهل):
    print("Correct.")
else:
    print("False.")