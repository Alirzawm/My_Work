import re
def check_name(علیرضا):

    if len(نام) > 10:
        return "باید حداکثر 10 کرکتر باشد."

    if not re.match("^[آ-ی]+$", نام):
        return "باید فقط شامل حروف فارسی باشد."

    if any(char.isdigit() or not char.isalnum() for char in نام):
        return "نباید حاوی عدد یا علائم خاص باشد."

    return "نامعتبر"

نام = input("علیرضا")

result = check_name(نام)
print(result)