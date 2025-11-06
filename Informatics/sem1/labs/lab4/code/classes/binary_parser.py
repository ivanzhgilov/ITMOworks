# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

from utils import BinaryConverter
from classes.section_classes import Sections, Section, Comments

class BinaryParser:

    def serialize_sections(self, sections: Sections):

        binary_data = bytearray()

        # Записываем количество секций (4 байта)
        binary_data.extend(BinaryConverter.int_to_bytes(sections.get_count_sections()))

        # noinspection PyCompatibility
        section: Section
        for section in sections.get_section_list():
            # Записываем длину имени секции и само имя
            section_name_bytes = section.get_name().encode('utf-8')
            binary_data.extend(BinaryConverter.int_to_bytes(len(section_name_bytes)))
            binary_data.extend(section_name_bytes)

            # Записываем количество пар ключ-значение в секции
            binary_data.extend(BinaryConverter.int_to_bytes(section.get_count()))

            # noinspection PyCompatibility
            data_section: list[tuple] = section.items()
            for key, value in data_section:

                # Записываем ключ
                key_bytes = key.encode('utf-8')
                binary_data.extend(BinaryConverter.int_to_bytes(len(key_bytes)))
                binary_data.extend(key_bytes)

                # Записываем значение
                value_bytes = value.encode('utf-8')
                binary_data.extend(BinaryConverter.int_to_bytes(len(value_bytes)))
                binary_data.extend(value_bytes)

        return binary_data

    def serialize_comment(self, comments: Comments):
        binary_comments = bytearray()
        # Записываем кол-во комментариев
        binary_comments.extend(BinaryConverter.int_to_bytes(comments.get_count_comment()))

        # noinspection PyCompatibility
        comment: tuple[int, int, str]
        for comment in comments.items():
            ind = comment[0]
            id_sect = comment[1]
            value = comment[2]
            # Записываем индекс и сам коммент
            binary_comments.extend(BinaryConverter.int_to_bytes(ind))
            binary_comments.extend(BinaryConverter.int_to_bytes(id_sect))
            value_bytes = value.encode('utf-8')
            binary_comments.extend(BinaryConverter.int_to_bytes(len(value_bytes)))
            binary_comments.extend(value_bytes)

        return binary_comments

    def combinate_comments_and_sections(self, comments: Comments, sections: Sections):
        return bytes(self.serialize_sections(sections)) + bytes(self.serialize_comment(comments))


    def save_to_file(self, filename, sections: Sections, comments: Comments):
        """Сохранение данных в бинарный файл"""
        binary_data = self.combinate_comments_and_sections(comments, sections)
        with open(filename, 'wb') as file:
            file.write(binary_data)
        return len(binary_data)

    def deserialize(self, binary_data):

        result_data = {}
        offset = 0

        # Читаем количество секций (4 байта)
        number_sections = BinaryConverter.bytes_to_int(binary_data, offset)
        offset += 4

        for _ in range(number_sections):
            # Читаем имя секции
            section_name_len = BinaryConverter.bytes_to_int(binary_data, offset)
            offset += 4
            section_name = binary_data[offset:offset + section_name_len].decode('utf-8')
            offset += section_name_len

            # Читаем количество пар ключ-значение
            num_pairs = BinaryConverter.bytes_to_int(binary_data, offset)
            offset += 4

            result_data[section_name] = {}

            for __ in range(num_pairs):
                # Читаем ключ
                key_len = BinaryConverter.bytes_to_int(binary_data, offset)
                offset += 4
                key = binary_data[offset:offset + key_len].decode('utf-8')
                offset += key_len

                # Читаем значение
                value_len = BinaryConverter.bytes_to_int(binary_data, offset)
                offset += 4
                value = binary_data[offset:offset + value_len].decode('utf-8')
                offset += value_len

                result_data[section_name][key] = value

        result_comments = []
        number_comments = BinaryConverter.bytes_to_int(binary_data, offset)
        offset += 4

        for _ in range(number_comments):

            ind = BinaryConverter.bytes_to_int(binary_data, offset)
            offset += 4
            id_sect = BinaryConverter.bytes_to_int(binary_data, offset)
            offset += 4
            comment_len = BinaryConverter.bytes_to_int(binary_data, offset)
            offset += 4
            comment = binary_data[offset:offset + comment_len].decode('utf-8')
            offset += comment_len

            result_comments.append([ind, id_sect, comment])

        return [result_data, result_comments]

    def load_from_file(self, filename):
        """Загрузка данных из бинарного файла"""
        with open(filename, 'rb') as file:
            binary_data = file.read()
        return self.deserialize(binary_data)