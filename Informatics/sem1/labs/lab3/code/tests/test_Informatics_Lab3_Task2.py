# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 18.10.2025

import pytest
from Informatics_Lab3_Task2 import mail_server_find


class TestMailServerFind:
    """Тесты для функции извлечения почтового сервера"""

    def test_valid_emails(self):
        """Тест корректных email адресов"""
        test_cases = [
            ("students.spam@yandex.ru", "yandex.ru"),
            ("example@example.com", "example.com"),
            ("user.name@mail.ru", "mail.ru"),
            ("test_user@google.com", "google.com"),
            ("abc123@domain.org", "domain.org"),
        ]

        for email, expected in test_cases:
            result = mail_server_find(email)
            assert result == expected, f"Ошибка для {email}: ожидалось {expected}, получено {result}"

    def test_invalid_emails(self):
        """Тест некорректных email адресов"""
        invalid_emails = [
            "google@.ru",
            "google.com@goomle.com@google.com",
            "ya@ya..ru"
            "example@example",  # нет домена верхнего уровня
            "invalid@server",  # нет точки в домене
            "user@123.com",  # цифры в домене
            "test@my-site.com",  # дефис в домене
            "user@domain..com",  # две точки подряд
            "@domain.com",  # нет локальной части
            "user@.com",  # нет имени домена
            "user@domain.",  # нет домена верхнего уровня
            "мояпочта@main.com" # русские символы
        ]

        for email in invalid_emails:
            result = mail_server_find(email)
            assert result == "Fail!", f"Ошибка для {email}: ожидалось 'Fail!', получено {result}"

    def test_special_characters(self):
        """Тест специальных символов"""
        test_cases = [
            ("user.name@domain.com", "domain.com"),  # точка в локальной части
            ("user_name@domain.com", "domain.com"),  # подчеркивание
            ("user-name@domain.com", "Fail!"),  # дефис не допускается
            ("user+tag@domain.com", "Fail!"),  # плюс не допускается
        ]

        for email, expected in test_cases:
            result = mail_server_find(email)
            assert result == expected, f"Ошибка для {email}: ожидалось {expected}, получено {result}"

    def test_edge_cases(self):
        """Тест граничных случаев"""
        test_cases = [
            ("test@sub.domain.com", "sub.domain.com"),  # несколько доменов верхнего уровня
            ("user.name@server.co.uk", "server.co.uk"),  # несколько доменов верхнего уровня
        ]

        for email, expected in test_cases:
            result = mail_server_find(email)
            assert result == expected, f"Ошибка для {email}: ожидалось {expected}, получено {result}"

    def test_string(self):
        """Тест строк без почты"""
        test_cases = [
            "I am just string",  # просто строка
            "I am string with email@mail.ru",  # строка с почтой, а должна быть только почта
        ]

        for email in test_cases:
            result = mail_server_find(email)
            assert result == "Fail!", f"Ошибка для {email}: ожидалось 'Fail!', получено {result}"

