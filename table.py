number = float(input("Укажите номер вещества"))


def get_name(number):
    if number == 3:
        return "Li"
    elif number == 25:
        return "Mn"
    elif number == 80:
        return "Hg"
    elif number == 17:
        return "Cl"
    else:
        return "Не найдено"

    
print(get_name(number))
