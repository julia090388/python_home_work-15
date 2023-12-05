# 1 – Дорабатываем задачу 4. Добавьте регистрацию возможных ошибок.
# Добавьте возможность запуска из командной строки с использованием библиотеки argparse

import logging
import datetime
from datetime import date, datetime
from collections import namedtuple
import argparse

logging.basicConfig(filename="log.log", encoding="utf8", level=logging.INFO)
logger = logging.getLogger("log")

MONTH = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}
WEEKDAYS = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}
DATE = namedtuple("DATE", "day month year")


def get_date(text):
    try:
        num_week, week_day, month = text.split()
        num_week = int(num_week.split("-")[0])
        week_day = WEEKDAYS[week_day]
        count_week = 0
        for day in range(1, 31 + 1):
            d = date(year=datetime.now().year, month=MONTH[month], day=day)
            if d.weekday() == week_day:
                count_week += 1
                if count_week == num_week:
                    logger.info(DATE(d.day, d.month, d.year))
                    return d
        raise ValueError("Неправильный формат текста")

    except (ValueError, KeyError) as e:
        logger.error(f"Ошибка при обработке текста: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(description='Дата из текста')
    parser.add_argument('text', help='Текст в формате "1-й четверг ноября"')
    args = parser.parse_args()

    date = get_date(args.text)
    if date:
        print(date)


if __name__ == '__main__':
    main()