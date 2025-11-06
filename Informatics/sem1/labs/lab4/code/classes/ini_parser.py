# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

from classes.section_classes import Sections, Section, Comments
from classes.errors import DuplicateKeyError, DuplicateSectionError, MissingSectionHeaderError, ParsingError
from utils import AnalyzerSyntaxis


class INIParser:
    def __init__(self) -> None:
        # noinspection PyCompatibility
        self._current_section: Section = None
        # noinspection PyCompatibility
        self._sections_list: Sections = Sections()
        # noinspection PyCompatibility
        self._comments_list: Comments = Comments()


    def read(self, filename: str) -> None:
        with open(filename, "r", encoding='utf-8') as file:
            text = file.readlines()

        source = filename.split("/")[-1]

        self._parse(text, source)

    def _parse_section(self, section_name: str) -> None:
        section = Section(section_name)
        self._current_section = section
        self._sections_list.add_section(section)

    def _parse_key_value(self, key: str, value: str) -> None:
        self._current_section.add_data(key.strip(), value.strip())

    def _parse_comment(self, ind: int, id_sect, string: str) -> None:
        self._comments_list.add_comment(ind, id_sect, string)

    def _parse(self, text, source) -> None:
            number_line = 0
            inf_line_number = 0
            numb_section = 0
            for line in text:
                number_line += 1
                string = line.strip()
                if string != "": # skip empty lines
                    inf_line_number += 1
                    if AnalyzerSyntaxis.is_comment(string):
                        self._parse_comment(inf_line_number, numb_section, string[1:])

                    elif AnalyzerSyntaxis.is_section(string):
                        numb_section += 1
                        section_name = string[1:-1]
                        if self._sections_list.has_section(section_name):
                            raise DuplicateSectionError(source, number_line, section_name)
                        self._parse_section(section_name)

                    elif AnalyzerSyntaxis.is_data(string):
                        if self._current_section is None:
                            raise MissingSectionHeaderError(source, number_line)
                        ind_sym_equals = string.find("=")
                        if ind_sym_equals == -1:
                            ind_sym_equals = len(string) + 1
                        ind_sym_colon = string.find(":")
                        if ind_sym_colon == -1:
                            ind_sym_colon = len(string) + 1

                        ind = min(ind_sym_equals, ind_sym_colon)

                        key = string[:ind]
                        value = string[ind + 1:]
                        if self._current_section.has_key(key):
                            raise DuplicateKeyError(source, number_line, key, self._current_section.get_name())
                        self._parse_key_value(key, value)

                    else:
                        raise ParsingError(source, number_line, string)
    def sections(self) -> list[str]:
        return self._sections_list.section_names

    def items(self, section_name) -> list:
        return self._sections_list.items_section(section_name)

    def get(self, section_name: str, key: str) -> str:
        return self._sections_list.get(section_name, key)

    def get_all_sections(self):
        return self._sections_list

    def get_all_comments(self) -> list[tuple[int, str]]:
        return self._comments_list


if __name__ == "__main__":
    parser = INIParser()
    parser.read("../data/schedule.ini")
    for name in parser.sections():
        print(parser.items(name))






