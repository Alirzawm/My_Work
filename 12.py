def check_major(مهندسی_کامپیوتر):
    engineering_majors = ["مهندسی کامپیوتر", "مهندسی برق", "مهندسی مکانیک", "مهندسی عمران", "مهندسی صنایع"]
    if مهندسی_کامپیوتر in engineering_majors:
        return True
    else:
        return False

رشته_کاربر = input("مهندسی کامپیوتر")
if check_major(رشته_کاربر):
    print("Correct")
else:
    print("False. My major is مهندسی کامپیوتر")