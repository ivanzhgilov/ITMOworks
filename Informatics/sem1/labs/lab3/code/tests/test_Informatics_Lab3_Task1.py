# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 18.10.2025

import pytest
from Informatics_Lab3_Task1 import mail_server_find


class TestSurnameFinder:
    """Тесты для функции поиска фамилий"""

    def test_regular_surnames(self):
        """Обычные фамилии с инициалами"""
        text = "На собрании были Иванов А.В., Петров С.К. и Сидоров Д.М."
        result = mail_server_find(text)
        expected = "Иванов\nПетров\nСидоров"
        assert result == expected

    def test_double_surnames(self):
        """Двойные фамилии с дефисами"""
        text = "Присутствовали Петрова-Сидорова М.К., Иванов-Смирнов П. и Козлов Д.В."
        result = mail_server_find(text)
        expected = "Иванов-Смирнов\nКозлов\nПетрова-Сидорова"
        assert result == expected

    def test_duplicate_surnames(self):
        """Повторяющиеся фамилии должны быть уникальными"""
        text = "Иванов А.В. выступил первым. Затем Иванов А.В. ответил на вопросы. Петров С.К. был третьим."
        result = mail_server_find(text)
        expected = "Иванов\nПетров"
        assert result == expected

    def test_edge_cases(self):
        """Пограничные случаи и ложные срабатывания"""
        text = """Москва .. не фамилия
         но подходит. Иванов А. без второй точки
        . Петров С.К. - фамилия. Река Волга красива."""
        result = mail_server_find(text)
        expected = "Иванов\nПетров"
        assert result == expected

    def test_no_surnames(self):
        """Текст без фамилий"""
        text = "В этом тексте нет фамилий с инициалами. Только обычные слова."
        result = mail_server_find(text)
        expected = ""
        assert result == expected

    def test_empty_string(self):
        """Пустая строка"""
        text = ""
        result = mail_server_find(text)
        expected = ""
        assert result == expected

    def test_surname_with_single_initial(self):
        """Фамилия с одним инициалом"""
        text = "Иванов А. - один инициал, Петров С.К. - два инициала, Добродеев"
        result = mail_server_find(text)
        expected = "Иванов\nПетров"
        assert result == expected

    def test_multiple_spaces(self):
        """Фамилии с разным количеством пробелов"""
        text = "Иванов  А.В., Петров С.    К., Сидоров   Д.М."
        result = mail_server_find(text)
        expected = "Иванов\nПетров\nСидоров"
        assert result == expected

    def test_surname_at_start_and_end(self):
        """ Фамилии в начале и конце текста"""
        text = "Иванов-Петров-Водкин А.В. начинает текст. А заканчивает Сидоров Д.М."
        result = mail_server_find(text)
        expected = "Сидоров"
        assert result == expected
