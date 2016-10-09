# -*- coding: utf-8 -*-
from json import dumps, load
from codecs import open
from os.path import exists


def load_data(filepath):
    if not exists(filepath):
        return None

    with open(filepath, 'r', 'utf-8') as file_handler:
        return load(file_handler)


def json_pretty_print(data):
    print(dumps(data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    filepath = input(u'Введите путь к файлу в формате json:')
    data = load_data(filepath)
    if data is None:
        print (u'Данных нет или указан неверный путь к файлу')
    else:
        json_pretty_print(data)
