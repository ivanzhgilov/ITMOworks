# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

from utils import AnalyzerSyntaxis


class XMLSerializer:

    def __init__(self):
        self._indent_level = 0

    def escape_xml(self, text):
        """Экранирование специальных XML символов"""
        if not text:
            return text

        escaped = text
        escapes = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&apos;'
        }

        for char, replacement in escapes.items():
            escaped = escaped.replace(char, replacement)

        return escaped

    def is_valid_xml_name(self, name):
        """Проверка валидности имени XML элемента"""
        if not name or not name.strip():
            return False

        # Первый символ должен быть буквой, underscore, или двоеточием
        first_char = name[0]
        if not AnalyzerSyntaxis.is_correct_first_sym_xml(first_char):
            return False

        # Остальные символы могут быть буквами, цифрами, и некоторыми специальными символами
        for char in name[1:]:
            if not AnalyzerSyntaxis.is_correct_other_sym_xml(char):
                return False

        return True

    def make_valid_xml_name(self, name):
        """Создание валидного имени XML элемента из произвольной строки"""
        if self.is_valid_xml_name(name):
            return name

        # Заменяем недопустимые символы на underscore
        valid_name = ""
        for i, char in enumerate(name):
            if i == 0:
                # Первый символ - только буквы или underscore
                if AnalyzerSyntaxis.is_correct_first_sym_xml(char):
                    valid_name += char
                else:
                    valid_name += '_'
            else:
                # Остальные символы - буквы, цифры, underscore, дефис, точка
                if AnalyzerSyntaxis.is_correct_other_sym_xml(char):
                    valid_name += char
                else:
                    valid_name += '_'

        # Если имя пустое после преобразования
        if not valid_name:
            valid_name = "item"

        return valid_name

    def get_indent(self):
        """Получить отступ для текущего уровня"""
        return "  " * self._indent_level

    def serialize_element(self, tag_name, content, is_attribute=False):
        """Сериализация XML элемента"""
        indent = self.get_indent()
        valid_tag = self.make_valid_xml_name(tag_name)

        if is_attribute:
            # Для атрибутов возвращаем пару имя=значение
            escaped_content = self.escape_xml(str(content))
            return f'{valid_tag}="{escaped_content}"'

        if isinstance(content, dict):
            # Элемент с вложенными элементами
            lines = [f'{indent}<{valid_tag}>']

            self._indent_level += 1
            for key, value in content.items():
                if isinstance(value, dict):
                    # Вложенный элемент
                    lines.append(self.serialize_element(key, value))
                else:
                    # Простой элемент
                    lines.append(self.serialize_element(key, value))
            self._indent_level -= 1

            lines.append(f'{indent}</{valid_tag}>')
            return '\n'.join(lines)

        else:
            # Простой элемент с текстовым содержимым
            escaped_content = self.escape_xml(str(content))
            return f'{indent}<{valid_tag}>{escaped_content}</{valid_tag}>'

    def serialize_section(self, section_name, section_data):
        """Сериализация секции INI в XML"""
        indent = self.get_indent()
        valid_section_name = self.make_valid_xml_name(section_name)

        lines = [f'{indent}<section name="{self.escape_xml(valid_section_name)}">']

        self._indent_level += 1
        for key, value in section_data.items():
            valid_key = self.make_valid_xml_name(key)
            escaped_value = self.escape_xml(value)
            lines.append(f'{self.get_indent()}<{valid_key}>{escaped_value}</{valid_key}>')
        self._indent_level -= 1

        lines.append(f'{indent}</section>')
        return lines

    def serialize_comment(self, body_comment, indent=""):
        line = '{}<!-- {} -->'.format(indent, body_comment)
        return line

    def serialize(self, data):
        """
        Сериализация словаря в формат XML

        Args:
            data: словарь вида {section: {key: value}}

        Returns:
            str: строка в формате XML
        """
        self._indent_level = 0

        xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<schedule>']

        data_dict = data[0]
        data_comment = data[1]

        self._indent_level += 1
        for section_name, section_data in data_dict.items():
            xml_lines += self.serialize_section(section_name, section_data)
        self._indent_level -= 1

        xml_lines.append('</schedule>')

        for comment in data_comment:
            ind = comment[0]
            id_section = comment[1]
            text = comment[2]
            print(comment)
            line = self.serialize_comment(text)
            index_comment = ind + id_section + 2
            xml_lines = xml_lines[:index_comment - 1] + [line] + xml_lines[index_comment - 1:]
            string_up = xml_lines[index_comment - 2]
            string_down = xml_lines[index_comment]
            indent = AnalyzerSyntaxis.get_max_indent(string_up, string_down)
            xml_lines[index_comment - 1] = indent + xml_lines[index_comment - 1]

        return '\n'.join(xml_lines)

    def save_to_file(self, data_dict, filename):
        """Сохранение данных в XML файл"""
        xml_content = self.serialize(data_dict)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(xml_content)
        return len(xml_content)
