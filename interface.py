from logger import logging
import functions as f
import check


def menu():
    print()
    print('Журнал заметок открыт\n')
    logging.info('Start program')
    while True:
        menu_item = input('Выберите пункт меню и введите соответсвующий номер:\n'
                          '1 - Показать все записи\n'
                          '2 - Найти запись\n'
                          '3 - Добавить запись\n'
                          '4 - Редактировать запись\n'
                          '5 - Удалить запись\n'
                          '0 - Выход\n')
        menu_item = check.check_is_digit(menu_item)

        if menu_item not in range(6):
            logging.warning('Warning: menu item does not exist')
            print("Вы ввели не существующий пункт меню. Попробуйте еще раз\n")

        # показать все записи
        if menu_item == 1:
            print('Весь перечень заметок:')
            f.print_notes('notes.csv')
            print('Вы будете перемещены в главное меню.\n')

        # найти запись
        if menu_item == 2:
            data = (input('Введите данные для поиска: ')).lower()
            find_id_list = f.find_info('notes.csv', data)
            if len(find_id_list) == 0:
               print('По вашему запросу ничего не найдено.\n')
            print('Вы будете перемещены в главное меню.\n')

        # добавить запись
        if menu_item == 3:
            print('Добавление новой записи')
            f.add_text('notes.csv')
            print('Вы будете перемещены в главное меню.\n')

        # редактировать запись
        if menu_item == 4:
            data = (input('Введите данные для поиска: ')).lower()
            find_list_id = f.find_info('notes.csv', data)
            if len(find_list_id) == 0:
                print("По вашему запросу ничего не найдено")
            else:
                entered_id = (input(
                    'Введите id записи, данные которой вы хотите изменить:\n')).lower()
                id = check.check_is_digit(entered_id)
                if id == -1:
                    logging.warning('Warning: Incorrect data entered')
                    print('Вы ввели некорректные данные\n')
                else:
                    exist_id = check.check_id_exist(id, find_list_id)
                    if exist_id == -1:
                        logging.warning('Warning: Incorrect id entered')
                        print('Ошибка ввода id заметки\n')
                    else:
                        change_item = input('\nВыберите вид изменения и введите соответствующий номер:\n'
                                    '1 - Изменить заметку\n'
                                    '2 - Изменить статус заметки\n'
                                    '3 - Изменить все данные\n')
                        int_change_item = check.check_is_digit(change_item)
                        if int_change_item in range(1, 4):
                            f.change_info('notes.csv', id, int_change_item)
                        else:
                            logging.warning('Warning: menu item does not exist')
                            print("Такой вид изменения не существует\n")
            print('Вы будете перемещены в главное меню.\n')
                            

        # удалить запись
        if menu_item == 5:
            data = (input('Введите данные для поиска: ')).lower()
            find_list_id = f.find_info('notes.csv', data)
            if len(find_list_id) == 0:
                print("По вашему запросу ничего не найдено")
            else:
                entered_id = (input('Введите id записи, которую хотите удалить:\n')).lower()
                id = check.check_is_digit(entered_id)

                if id == -1:
                    logging.warning('Warning: Incorrect data entered')
                    print('Вы ввели некорректные данные\n')
                else:
                    exist_id = check.check_id_exist(id, find_list_id)
                    if exist_id == -1:
                        logging.warning('Warning: Incorrect id entered')
                        print('Ошибка ввода id заметки\n')
                    else:
                        f.delete_info('notes.csv', exist_id)
            print('Вы будете перемещены в главное меню.\n')

        # выход
        if menu_item == 0:
            logging.info("Finish program")
            print('Спасибо, что воспользовались нашим журналом заметок\n')
            break
