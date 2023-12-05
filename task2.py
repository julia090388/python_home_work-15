# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.

import os
import logging
from collections import namedtuple

logging.basicConfig(filename='log.txt', level=logging.INFO)

ContentItem = namedtuple('ContentItem', ['name', 'extension', 'is_directory', 'parent_directory'])


def process_directory(directory_path):
    content = os.listdir(directory_path)
    for item in content:
        item_path = os.path.join(directory_path, item)
        is_directory = os.path.isdir(item_path)
        name, extension = os.path.splitext(item)

        content_item = ContentItem(name, extension, is_directory, directory_path)
        logging.info(content_item)

        if is_directory:
            process_directory(item_path)


if __name__ == '__main__':

    directory_path = input('Введите путь до директории: ')

    if not os.path.isdir(directory_path):
        print('Указанная директория не существует.')
    else:

        process_directory(directory_path)