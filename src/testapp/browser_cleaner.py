import datetime
import os
# Модуль для работы с регулярными выражениями
import re
def parsing():
    PROJECT_DIR = os.path.dirname(__file__)
    DB_FILE = os.path.join(PROJECT_DIR, "brwsr_req.txt")
    fp = open(DB_FILE, "r")
    query_lst = list()
    for unrefined_string in fp:
        delimiters = ' - -', ' [', '] ', '"'
        regexPattern = '|'.join(map(re.escape, delimiters))
        elements_list = re.split(regexPattern, unrefined_string)
        elements_list[2] = (datetime.datetime.strptime(elements_list[2],
                            '%d/%B/%Y:%H:%M:%S %z')).date()
        adjusted_list = []
        adjusted_list.append(elements_list[0])
        adjusted_list.append(elements_list[2])
        if "Safari" in elements_list[8]:
            adjusted_list.append("Safari")
        else:
            adjusted_list.append("-")
        if "Firefox" in elements_list[8]:
            adjusted_list.append("Firefox")
        else:
            adjusted_list.append("-")
        adjusted_list.append(unrefined_string)
        query_lst.append(adjusted_list)
    fp.close()
    return query_lst
a = parsing()
print(len(a))
if __name__=="__main__":
    parsing()