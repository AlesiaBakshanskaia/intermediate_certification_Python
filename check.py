import functions as f
from os import path


def check_menu_item(menu_item: str) -> int:
    if menu_item.isdigit():
        return int(menu_item)
    return -1

# проверка существования id
def check_id_exist(id: int, id_list: list) -> int:
    count = 0
    for i in range(len(id_list)):
        if int(id_list[i]) == id:
            count += 1
    if count > 0:
        return id
    else:
        return -1
