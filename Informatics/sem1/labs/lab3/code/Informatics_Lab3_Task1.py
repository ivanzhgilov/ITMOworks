# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 18.10.2025
# Variant 3
import re
import sys

"""Функция для тестов"""

def mail_server_find(input_text: str):
    pattern = r"(?:\s|^)([А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+){0,1})\s+(?:[А-ЯЁ]\.){1,2}"
    result = re.findall(pattern, input_text)

    result = list(set(result))

    result.sort()

    result_string = ""
    for i in range(len(result)):
        result_string += result[i]
        if i != len(result) - 1:
            result_string += "\n"

#    result_string = "\n".join(result)

    return result_string

"""Для запуска программы"""

if __name__ == '__main__':
    text = sys.stdin.read()
    print(mail_server_find(text))
