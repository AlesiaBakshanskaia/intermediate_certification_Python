from os import path
import csv
from prettytable import PrettyTable
import sys
import datetime
from logger import logging


def last_id():
    with open('last_id.txt', 'r', encoding='utf-8') as l_f:
        last_id = l_f.read()
        return last_id

# дозапись


def write_file(file, data):
    with open(file, 'a', encoding='utf-8') as t_file:
        file_writer = csv.writer(t_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(data)


# перезапись

def write_file_w(file, data):
    with open(file, 'w', encoding='utf-8') as t_file:
        file_writer = csv.writer(t_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(data)

# чтение


def read_file(file):
    if path.exists(file):
        with open(file, 'r', encoding='utf-8') as t_file:
            csv.reader(t_file, delimiter=';')
            all_notes = []
            for row in t_file:
                str_note = "".join(row)
                list_pers = str_note.strip().split(';')
                all_notes.append(list_pers)
        return all_notes
    else:
        logging.error(f'Файл {file} не существует')
        print("Файл не существует")

# вывод всех заметок


def print_notes(file):
    list_all_notes = read_file(file)
    table = PrettyTable(list_all_notes[0])
    for i in range(1, len(list_all_notes)):
        table.add_row(list_all_notes[i])
    print(table)

# поиск


def find_info(file, data):
    find_list = []
    list_all_notes = read_file(file)
    for i in range(1, len(list_all_notes)):
        for j in range(len(list_all_notes[i])):
            if str(list_all_notes[i][j]).find(data) == -1:
                pass
            else:
                find_list.append(list_all_notes[i])
                break
    for k in range(len(find_list)+1):
        if k == 0:
            write_file_w('file_for_search.csv', list_all_notes[k])
        else:
            write_file('file_for_search.csv', find_list[k-1])
    print('Информация по вашему запросу.')
    print_notes('file_for_search.csv')


# дозапись
def add_text(file):
    id = last_id()
    id = int(id) + 1
    id_w = str(id)
    with open('last_id.txt', 'w', encoding='utf-8') as l_f:
        l_f.write(id_w)
    date = get_date()
    note = input('Введите заметку: ')
    status = input('Введите статус: ')
    new_person = [id, date, note, status]
    write_file(file, new_person)
    print('Заметка успешно добавлена')
    print('Обновлённый список заметок')
    print_notes('notes.csv')

# замена


def change_info(file, id, operation):
    list_all_notes = read_file(file)
    for i in range(1, len(list_all_notes)):
        if list_all_notes[i][0] == str(id):
            list_all_notes[i][1] = get_date()
            if operation == 1:
                list_all_notes[i][2] = input('Перепешите заметку: ')
            elif operation == 2:
                list_all_notes[i][3] = input('Измените статус заметки: ')
            elif operation == 3:
                list_all_notes[i][2] = input('Перепешите заметку: ')
                list_all_notes[i][3] = input('Измените статус заметки: ')

    for j in range(len(list_all_notes)):
        if j == 0:
            write_file_w(file, list_all_notes[j])
        else:
            write_file(file, list_all_notes[j])
    print('Заметка успешно изменена')
    print('Обновлённый список заметок')
    print_notes('notes.csv')


# удаление
def delete_info(file, m_id):
    ist_all_notes = read_file(file)
    for i in range(1, len(ist_all_notes)):
        if ist_all_notes[i][0] == str(m_id):
            ist_all_notes.pop(i)
            break
    for j in range(len(ist_all_notes)):
        if j == 0:
            write_file_w(file, ist_all_notes[j])
        else:
            write_file(file, ist_all_notes[j])
    print('Заметка успешно удалена')
    print('Обновлённый список заметок"')
    print_notes('notes.csv')
    

def get_date():
    now = datetime.datetime.now()
    day = str(now.day)
    year = str(now.year)
    monthint = now.month
    if monthint < 10:
        date = day + "-" + "0" + str(monthint) + "-" + year
    else:
        date = day + "-" + str(monthint) + "-" + year
    return date
