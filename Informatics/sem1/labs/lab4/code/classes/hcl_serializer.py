# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

from utils import AnalyzerSyntaxis


class HCLSerializer:

    # Использовал для заключения ключа в кавычки, на практике с библиотечным парсером не работает.
    # В целом для нашего файла это и не нужно
    # def is_valid_identifier(self, identifier):
    #     """Проверка валидности идентификатора HCL"""
    #     if not identifier:
    #         return False
    #
    #     # Первый символ должен быть буквой или underscore
    #     first_char = identifier[0]
    #     if Analyzer.is_correct_first_sym_hcl(first_char):
    #         return False
    #
    #     # Остальные символы могут быть буквами, цифрами, underscore, дефис
    #     for char in identifier[1:]:
    #         if not Analyzer.is_correct_other_sym_hcl(char):
    #             return False
    #
    #     return True

    def escape_string(self, value):
        """Экранирование строки для HCL"""

        # Проверяем, нужно ли заключать в кавычки
        needs_quotes = any(not AnalyzerSyntaxis.is_correct_other_sym_hcl(char) for char in value)

        escaped = value

        if needs_quotes:
            escaped = ""
            for char in value:
                if char == '\\':
                    escaped += '\\\\'
                elif char == '\n':
                    escaped += '\\n'
                elif char == '\t':
                    escaped += '\\t'
                elif char == '\r':
                    escaped += '\\r'
                elif char == '\f':
                    escaped += '\\f'
                elif char == '\v':
                    escaped += '\\v'
                elif char == '"':
                    escaped += '\\"'
                else:
                    escaped += char  # / остается как есть, но в кавычках
        return f'"{escaped}"'

    # Прикольная фича, но на практике автоматически изменять типы переменных может быть не лучшей идеей
    # def format_value(self, value):
    #     """Форматирование значения для HCL"""
    #     # Проверяем, является ли значение числом
    #     if Analyzer.is_numeric(value):
    #         return value
    #
    #     # Проверяем, является ли значение булевым
    #     if value.lower() in ('true', 'false'):
    #         return value.lower()
    #
    #     # Проверяем, является ли значение null
    #     if value.lower() == 'null':
    #         return value
    #
    #     # В остальных случаях - строка
    #     return self.escape_string(value)

    def serialize_block(self, block_type, block_name, attributes):
        hcl_lines = []

        # Открываем блок
        if block_name:
            hcl_lines.append(f'{block_type} "{block_name}" {{')
        else:
            hcl_lines.append(f'{block_type} {{')

        # Добавляем атрибуты
        for key, value in attributes.items():
            formatted_value = self.escape_string(value)
            hcl_lines.append(f'  {key} = {formatted_value}')

        # Закрываем блок
        hcl_lines.append('}')

        return hcl_lines

    def serialize(self, data):
        """
        Сериализация словаря в формат HCL

        Args:
            data: словарь вида {section: {key: value}}

        Returns:
            str: строка в формате HCL
        """
        sections = data[0]
        comments = data[1]

        hcl_blocks = []

        for section_name, section_data in sections.items():
            # Преобразуем имя секции в валидный идентификатор HCL
            block_name = section_name

            # Создаем блок для каждой секции
            block = self.serialize_block("block", block_name, section_data)
            hcl_blocks += block

        for comment in comments:
            ind = comment[0]
            id_section = comment[1]
            text = comment[2]
            index_comment = ind + id_section
            hcl_blocks = hcl_blocks[:index_comment - 1] + ['#' + text] + hcl_blocks[index_comment - 1:]


        return "\n".join(hcl_blocks)  # возвращаем строку в HCL формате

    def save_to_file(self, data_dict, filename):
        hcl_content = self.serialize(data_dict)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(hcl_content)
        return len(hcl_content)
