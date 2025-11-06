# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

class AnalyzerSyntaxis:
    @staticmethod
    def is_whitespace(char) -> bool:
        return char in ' \t\n\r'

    @staticmethod
    def skip_whitespaces(string) -> str:
        result = ""
        for char in string:
            if not AnalyzerSyntaxis.is_whitespace(char):
                result += char
        return result

    @staticmethod
    def is_numeric(value):
        """Проверка, является ли значение числом"""
        try:
            int(value)
            return True
        except ValueError:
            try:
                float(value)
                return True
            except ValueError:
                return False


    @staticmethod
    def is_digit(char) -> bool:
        return "0" <= char <= "9"

    @staticmethod
    def is_letter(char) -> bool:
        return "a" <= char <= "z" or "A" <= char <= "Z" or char == "_"

    @staticmethod
    def is_alphanumeric(char) -> bool:
        return AnalyzerSyntaxis.is_digit(char) or AnalyzerSyntaxis.is_letter(char)

    @staticmethod
    def is_correct_first_sym_hcl(char) -> bool:
        return AnalyzerSyntaxis.is_letter(char)

    @staticmethod
    def is_correct_other_sym_hcl(char) -> bool:
        return AnalyzerSyntaxis.is_alphanumeric(char) or char == "-"

    @staticmethod
    def is_correct_first_sym_xml(char) -> bool:
        return AnalyzerSyntaxis.is_alphanumeric(char) or char == ":" or char == "_"

    @staticmethod
    def is_correct_other_sym_xml(char) -> bool:
        return AnalyzerSyntaxis.is_correct_first_sym_xml(char) or char == "." or char == "-"

    @staticmethod
    def is_section(string: str) -> bool:
        return string[0] == "[" and string[-1] == "]"

    @staticmethod
    def is_comment(string: str) -> bool:
        return string.startswith("#") or string.startswith(";")

    @staticmethod
    def is_data(string: str) -> bool:
        return not (AnalyzerSyntaxis.is_section(string)) and ("=" in string or ":" in string)

    @staticmethod
    def get_indent(string: str) -> str:
        indent = ""
        for char in string:
            if char == " ":
                indent += " "
            else:
                return indent
        return indent

    @staticmethod
    def get_max_indent(string_up: str, string_down: str) -> str:
        indent_up = AnalyzerSyntaxis.get_indent(string_up)
        indent_down = AnalyzerSyntaxis.get_indent(string_down)
        return indent_up if len(indent_up) > len(indent_down) else indent_down



class BinaryConverter:

    @staticmethod
    def int_to_bytes(n):
        """Конвертация целого числа в 4 байта"""
        return bytes([
            (n >> 24) & 0xFF,
            (n >> 16) & 0xFF,
            (n >> 8) & 0xFF,
            n & 0xFF
        ])

    @staticmethod
    def bytes_to_int(data, offset):
        """Конвертация 4 байт в целое число"""
        return (
                (data[offset] << 24) |
                (data[offset + 1] << 16) |
                (data[offset + 2] << 8) |
                data[offset + 3]
        )
