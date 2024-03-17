def check_birthplace_province(لرستان):
    provinces_centers = {
        "تهران": "تهران",
        "اصفهان": "اصفهان",
        "مازندران": "ساری",
        "فارس": "شیراز",
        "خراسان رضوی": "مشهد",
        "لرستان": "خرم آباد",

    }

    if birthplace_province in provinces_centers.values():
        print("Correct")
    else:
        print("False")

birthplace_province = input("Lorestan")

check_birthplace_province(birthplace_province)