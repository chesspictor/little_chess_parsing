import re
from datetime import datetime

#проверка, что это дата, используя регулярные выражения
def is_date(s):
    pattern = r'[0-3][0-9]\.[0-1][0-9]\.[0-9]{4}'
    s = s.replace('/', '.', 2)
    s = s.replace('-', '.', 2)
    s = s.strip()
    if len(s) > 10:
        return False
    elif len(s) == 9:
        s = '0' + s 
    if re.match(pattern, s):
        if int(s[:2]) > 31:
            return False
        else:
            if int(s[3:5]) == 2:
                if int(s[:2]) > 29:
                    return False
                elif int(s[:2]) == 29:
                    if int(s[6:10]) % 4 != 0:
                        return False
                    else:
                        if int(s[6:10]) % 100 == 0:
                            if int(s[6:10]) % 400 != 0:
                                return False
            elif int(s[3:5]) > 12:
                return False
            elif int(s[:2]) == 31:
                if int(s[3:5]) in [4, 6, 9, 11]:
                    return False
        return True
    else:
        return False

#перевод даты в номер недели для парсинга
def date_to_week_number(s):
    year = int(s[6:10])
    month = int(s[3:5])
    day = int(s[:2])
    date_user = datetime(year, month, day)
    date_base = datetime(2012, 6, 25)
    if date_user <= date_base:
        return 920
    diff = date_user - date_base
    return 920 + diff.days//7
