from logger import logging
import functions as f
import check


def menu():
    print()
    print('Журнал заметок открыт\n')
    logging.info('Приложение запущено')
    while True:
        menu_item = input('\nВыберите пункт меню и введите соответсвующий номер:\n'
                          '1 - Показать все записи\n'
                          '2 - Найти запись\n'
                          '3 - Добавить запись\n'
                          '4 - Редактировать запись\n'
                          '5 - Удалить запись\n'
                          '0 - Выход\n')
        menu_item = check.check_menu_item(menu_item)

        if menu_item not in range(6):
            logging.error('Error: введен не существующий пункт меню')
            print("Вы ввели не существующий пункт меню. Попробуйте еще раз\n")
            continue

        # показать все записи
        if menu_item == 1:
            print('Весь перечень заметок:')
            f.print_notes('notes.csv')
            print('Вы будете перемещены в главное меню.\n')
            continue

        # найти запись
        if menu_item == 2:
            d = (input('Введите данные для поиска: '))
            f.find_info('notes.csv', d)
            print('Вы будете перемещены в главное меню.\n')
            continue

        # добавить запись
        if menu_item == 3:
            print('Добавление новой записи')
            f.add_text('notes.csv')
            print('Вы будете перемещены в главное меню.\n')
            continue

        # редактировать запись
        if menu_item == 4:
            data = (input('Введите данные для поиска: '))
            f.find_info('notes.csv', data)
            entered_id = input(
                'Введите id записи, данные которой вы хотите изменить:\n')
            id = check.check_menu_item(entered_id)
            if id == -1:
                logging.error('Введены некорректные данные')
                print('Вы ввели некорректные данные\n')
            else:
                exist_id = check.check_id_exist('notes.csv', id)
                if exist_id == -1:
                    logging.error(f'Введен не существующий id {exist_id}')
                    print(f'Заметки с id {exist_id} не существует\n')
                else:
                    change_item = input('\nВыберите вид изменения и введите соответствующий номер:\n'
                                '1 - Изменить заметку\n'
                                '2 - Изменить статус заметки\n'
                                '3 - Изменить все данные\n')
                    int_change_item = check.check_menu_item(change_item)
                    if int_change_item in range(1, 4):
                        f.change_info('notes.csv', id, int_change_item)
                        print('Вы будете перемещены в главное меню.\n')
                    else:
                        logging.error('Введен не существующий вариант меню изменений')
                        print("Такой вид изменения не существует\n")
                        continue
            continue

        # удалить запись
        if menu_item == 5:
            data = (input('Введите данные для поиска: '))
            f.find_info('notes.csv', data)
            entered_id = input('Введите id записи, которую хотите удалить:\n')
            id = check.check_menu_item(entered_id)

            if id == -1:
                logging.error('Введены некорректные данные')
                print('Вы ввели некорректные данные\n')
            else:
                exist_id = check.check_id_exist('notes.csv', id)
                if exist_id == -1:
                    logging.error(f'Введен не существующий id {exist_id}')
                    print(f'Заметки с id {exist_id} не существует\n')
                else:
                    f.delete_info('notes.csv', exist_id)
            print('Вы будете перемещены в главное меню.\n')
            continue

        # выход
        if menu_item == 0:
            logging.info("Робота приложения завершена")
            print('Спасибо, что воспользовались нашим журналом заметок\n')
            break
