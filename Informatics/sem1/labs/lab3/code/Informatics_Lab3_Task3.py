# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 18.10.2025
# Variant 2
import re

"""Функция для тестов"""


def checking_password_requirements(password: str):
#    main_password_pattern = r"^(?=.*(january|february|march|april|may|june|july|august|september|october|november|december))(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{5,}$"
#    match = re.findall(main_password_pattern, password, re.IGNORECASE)
    password_pattern_1 = r".{5,}"
    password_pattern_2 = r"\d"
    password_pattern_3 = r"[A-Z]"
    password_pattern_4 = r"[^a-zA-Z0-9]"
    password_pattern_5 = r"\d"
    check_rule_5 = bool(sum(map(int, re.findall(password_pattern_5, password))) == 25)
    password_pattern_6 = r"(?i)(january|february|march|april|may|june|july|august|september|october|november|december)"
    password_patterns = [password_pattern_1, password_pattern_2, password_pattern_3, password_pattern_4,
                         password_pattern_5, password_pattern_6]
    password_requirements = ["Ваш пароль должен содержать минимум пять символов",
                             "Ваш пароль должен содержать цифры",
                             "Ваш пароль должен содержать заглавные буквы",
                             "Ваш пароль должен содержать специальные символы",
                             "Цифры в вашем пароле должны в сумме давать 25",
                             "Ваш пароль должен включать название месяца"]

    result = "Пароль подходит всем требованиям"

    errors_message = []
    for i in range(6):
        if i == 4:
            if not check_rule_5:
                errors_message.append(f"Rule {i + 1}: {password_requirements[i]}")
        else:
            if not re.findall(password_patterns[i], password):
                errors_message.append(f"Rule {i + 1}: {password_requirements[i]}")

    if errors_message:
        result = "\n".join(errors_message)

    return result


"""Для запуска программы"""

if __name__ == '__main__':
    text = input("Ведите пароль, который хотите проверить на корректность:\t")
    print(checking_password_requirements(text))
