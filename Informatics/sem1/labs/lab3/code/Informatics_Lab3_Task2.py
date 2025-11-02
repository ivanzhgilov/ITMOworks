# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 18.10.2025
# Variant 0
import re

"""Функция для тестов"""

def mail_server_find(string: str):
    pattern = r"^[A-Za-z0-9_.]+@([a-z]+(\.[a-z]+)+)$"
    match = re.match(pattern, string)
    result = "Fail!"
    if match:
        result = match.group(1)

    return result

"""Для запуска программы"""

if __name__ == '__main__':
    text = input("Ведите email, который хотите проверить на корректность:\t").strip()
    print(mail_server_find(text))
