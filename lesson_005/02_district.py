from district.central_street.house1.room1 import folks as centr_house_1_room_1
from district.central_street.house1.room2 import folks as centr_house_1_room_2
from district.central_street.house2.room1 import folks as centr_house_2_room_1
from district.central_street.house2.room2 import folks as centr_house_2_room_2
from district.soviet_street.house1.room1 import folks as sov_house_1_room_1
from district.soviet_street.house1.room1 import folks as sov_house_1_room_2
from district.soviet_street.house1.room2 import folks as sov_house_2_room_1
from district.soviet_street.house1.room2 import folks as sov_house_2_room_2

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

all_residents = []
all_residents.extend(centr_house_1_room_1)
all_residents.extend(centr_house_1_room_2)
all_residents.extend(centr_house_2_room_1)
all_residents.extend(centr_house_2_room_2)
all_residents.extend(sov_house_1_room_1)
all_residents.extend(sov_house_1_room_2)
all_residents.extend(sov_house_2_room_1)
all_residents.extend(sov_house_2_room_2)

print(f'На районе живут: {", ".join(all_residents)}')