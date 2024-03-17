def validate_melli_code(کدملی):
    if len(کدملی) != 10 or not کدملی.isdigit():
        return False

    check = int(کدملی[9])
    sum_ = sum(int(کدملی[i]) * (10 - i) for i in range(9)) % 11
    return (sum_ < 2 and check == sum_) or (sum_ >= 2 and check + sum_ == 11)

کد_ملی = input("4160741754")
if validate_melli_code(کد_ملی):
    print("Correct")
else:
    print("False")