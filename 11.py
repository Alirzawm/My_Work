def check_department(دانشکده):
    valid_departments = ["فنی و مهندسی", "علوم پایه", "علوم انسانی", "دامپزشکی", "اقتصاد", "کشاورزی", "منابع طبیعی"]
    if دانشکده in valid_departments:
        return True
    else:
        return False

نام_دانشکده = input("فنی و مهندسی")
if check_department(نام_دانشکده):
    print("Correct")
else:
    print("False")