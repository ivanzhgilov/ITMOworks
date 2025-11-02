# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 18.10.2025

import pytest
from Informatics_Lab3_Task3 import checking_password_requirements


class TestPasswordRequirements:

    def test_valid_password(self):
        """Тест корректного пароля, который проходит все проверки"""
        valid_password = "KL4D0VK4_P4VLU*xx!2JANuary ju1y23>131"
        result = checking_password_requirements(valid_password)
        assert result == "Пароль подходит всем требованиям"

    def test_short_password(self):
        """Тест пароля короче 5 символов"""
        short_password = "Ab1!"
        result = checking_password_requirements(short_password)
        assert "Rule 1:" in result

    def test_no_digits(self):
        """Тест пароля без цифр"""
        no_digit_password = "Hello_World!"
        result = checking_password_requirements(no_digit_password)
        assert "Rule 2:" in result

    def test_no_uppercase(self):
        """Тест пароля без заглавных букв"""
        no_upper_password = "hello123!"
        result = checking_password_requirements(no_upper_password)
        assert "Rule 3:" in result

    def test_no_special_chars(self):
        """Тест пароля без специальных символов"""
        no_special_password = "Hello123World"
        result = checking_password_requirements(no_special_password)
        assert "Rule 4:" in result

    def test_no_month(self):
        """Тест пароля без названия месяца"""
        no_month_password = "Hello123!World"
        result = checking_password_requirements(no_month_password)
        assert "Rule 6:" in result

    def test_multiple_errors(self):
        """Тест пароля с несколькими ошибками"""
        bad_password = "hi"  # Короткий, нет цифр, нет заглавных, нет спецсимволов, нет месяца
        result = checking_password_requirements(bad_password)

        # Проверяем наличие нескольких ошибок
        assert "Rule 1:" in result
        assert "Rule 2:" in result
        assert "Rule 3:" in result
        assert "Rule 4:" in result
        assert "Rule 5:" in result
        assert "Rule 6:" in result

        # Проверяем, что ошибки выводятся в правильном порядке
        lines = result.split('\n')
        assert lines[0].startswith("Rule 1:")
        assert lines[1].startswith("Rule 2:")
        assert lines[2].startswith("Rule 3:")
        assert lines[3].startswith("Rule 4:")
        assert lines[4].startswith("Rule 5:")
        assert lines[5].startswith("Rule 6:")

    def test_digit_sum_rule_always_fails(self):
        """Тест, что правило 5 (сумма цифр) всегда не выполняется"""
        password_with_digits = "Hello123!july"  # Сумма цифр 1+2+3=6 ≠ 25
        result = checking_password_requirements(password_with_digits)
        assert "Rule 5: Цифры в вашем пароле должны в сумме давать 25" in result

        password_sum_25 = "Hello997!july"  # Сумма цифр 9+9+7=25
        result = checking_password_requirements(password_sum_25)
        assert "Rule 5:" not in result

    def test_different_months(self):
        """Тест различных месяцев"""
        months = ["january", "february", "march", "april", "may", "june",
                  "july", "august", "september", "october", "november", "december"]

        for month in months:
            password = f"Ab1!{month}"
            result = checking_password_requirements(password)
            assert "Rule 6:" not in result

    def test_month_case_insensitive(self):
        """Тест регистронезависимости названий месяцев"""
        test_cases = [
            "JANUARY",
            "February",
            "mArCh",
            "APRIL",
            "May"
        ]

        for month in test_cases:
            password = f"Ab1!{month}"
            result = checking_password_requirements(password)
            assert "Rule 6:" not in result

    def test_empty_password(self):
        """Тест пустого пароля"""
        result = checking_password_requirements("")
        assert "Rule 1:" in result
        assert "Rule 2:" in result
        assert "Rule 3:" in result
        assert "Rule 4:" in result
        assert "Rule 5:" in result
        assert "Rule 6:" in result

    def test_only_special_chars(self):
        """Тест пароля только из специальных символов"""
        special_only = "!@#$%"
        result = checking_password_requirements(special_only)
        assert "Rule 2:" in result  # Нет цифр
        assert "Rule 3:" in result  # Нет заглавных
        assert "Rule 5:" in result  # Нет заглавных
        assert "Rule 6:" in result  # Нет месяца