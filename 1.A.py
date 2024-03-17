def get_student_info(شماره_دانشجویی):
    if len(شماره_دانشجویی) != 11:
        return "باید 11 رقم باشد."

    if شماره_دانشجویی[:6] != "114150":
        return "نامعتبر"

    index = شماره_دانشجویی[6:]
    if not index.isdigit() or not (1 <= int(index) <= 99):
        return "باید یک عدد بین 01 و 99 باشد"

    return {
        "شماره دانشجویی": شماره_دانشجویی,
        "سال": شماره_دانشجویی[2:4],
        "اندیس": int(index)
    }

شماره_دانشجویی = input("2402408")
result = get_student_info(شماره_دانشجویی)
print(result)