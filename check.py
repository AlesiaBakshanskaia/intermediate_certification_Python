import functions as f
from os import path


def check_menu_item(menu_item: str) -> int:
    if menu_item.isdigit():
        return int(menu_item)
    return -1

# проверка существования id
def check_id_exist(file, id: int) -> int:
    list_all_notes = f.read_file(file)
    temp = str(id)
    count = 0
    for i in range(1, len(list_all_notes)):
        if list_all_notes[i][0] == temp:
            count += 1
    if count > 0:
        return id
    else:
        return -1
