import re

car_plate_numbers = input()

def is_taxi(text):
    return re.fullmatch("[АВЕКМНОРСТУХ]{2}[0-9]{3}[0-9]{2,3}", text)
def is_private(text):
    return re.fullmatch("[АВЕКМНОРСТУХ][0-9]{3}[АВЕКМНОРСТУХ]{2}[0-9]{2,3}", text)

result = ""

for car_plate_number in car_plate_numbers.split():
    if is_taxi(car_plate_number) is not None:
        result += "Такси"
    elif is_private(car_plate_number) is not None:
        result += "Частный"
    else:
        result += "Не номер"
    result += " "

print(result)