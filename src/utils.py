from config import INDEX_CHAR_RANGE
import re

MONTH_MAP = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
           'September': 9, 'October': 10, 'November': 11, 'December': 12}

def create_page_index():
    """
    :return: list: [ '/','/a', '/b', '/c', '/d', ...,'/z']
    """
    list_of_char_index = ['']
    for char_index in range(INDEX_CHAR_RANGE):
        list_of_char_index.append(f"/{chr(ord('a') + char_index)}")
    return list_of_char_index


def time_transfer(time_string):
    hour_pattern = r'(\d*)(?=hr)'
    minute_pattern = r'(\d*)(?=m)'
    hour = re.search(hour_pattern, time_string)

    hour = int(hour.group()) if hour else 0
    minute = re.search(minute_pattern, time_string)
    minute = int(minute.group()) if minute else 0
    time_duration = hour*60+minute
    return time_duration


def date_transfer(time_stamp_string):
    pattern = r'(\d+)\w* (\w+) (\d+)(?= )'
    time_stamp = re.search(pattern, time_stamp_string)
    try:
        year = time_stamp.group(3)
        day = time_stamp.group(1)
    except AttributeError:
        return None, None, None
    month = time_stamp.group(2)
    month_n = MONTH_MAP[month]
    date_stamp = year+'/'+str(month_n)+'/'+day
    month_in_the_year = int(year)*12 + int(month_n) # 2020 Dec = 2020*12+ 12
    return date_stamp, month_in_the_year, year


def pattern_search(pattern, search_string):
    return re.search(pattern, search_string)
