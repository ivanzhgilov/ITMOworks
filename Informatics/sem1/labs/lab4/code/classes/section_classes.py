# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

from classes.errors import NoSectionError, NoKeyError

class Section:
    def __init__(self, name: str) -> None:
        self._name = name
        self._data = {}
        self._keys = []

    def add_data(self, key: str, value: str) -> None:
        self._data[key] = value
        self._keys.append(key)

    def has_key(self, key: str) -> bool:
        return key in self._keys

    def items(self):
        result = []
        for key, value in self._data.items():
            result.append((key, value))
        return result

    def get_value(self, key: str) -> str:
        return self._data[key]

    def get_count(self) -> int:
        return len(self._data)

    def get_name(self) -> str:
        return self._name


    def __str__(self) -> str:
        result = "[{}]\n".format(self._name)
        for key, value in self._data.items():
            result += ("{}={}\n".format(key, value))
        return result

    @property
    def data(self):
        return self._data


class Sections:
    def __init__(self) -> None:
        # noinspection PyCompatibility
        self._list_sections: list[Section] = []
        self.section_names = []

    def add_section(self, section: Section) -> None:
        self._list_sections.append(section)
        self.section_names.append(section.get_name())

    def has_section(self, section_name) -> bool:
        return section_name in self.section_names

    def items_section(self, section_name) -> dict:
        if not self.has_section(section_name):
            raise NoSectionError(section_name)

        index = self.section_names.index(section_name)
        return self._list_sections[index]._data

    def get(self, section_name: str, key: str) -> str:
        if not self.has_section(section_name):
            raise NoSectionError(section_name)

        index = self.section_names.index(section_name)
        section = self._list_sections[index]
        if not section.has_key(key):
            raise NoKeyError(section_name, key)

        return section.get_value(key)

    def get_count_sections(self) -> int:
        return len(self.section_names)

    def get_section_names(self) -> list:
        return self.section_names

    def get_section_list(self):
        return self._list_sections


    def __str__(self) -> str:
        result = ""
        for section in self._list_sections:
            result += str(section) + "\n"
        return result

class Comments:
    def __init__(self) -> None:
        # noinspection PyCompatibility
        self._list_comments: list[tuple[int, int, str]] = []

    def add_comment(self, ind: int, id_sect, comment: str,) -> None:
        self._list_comments.append(tuple([ind, id_sect, comment]))


    def get_count_comment(self) -> int:
        return len(self._list_comments)

    def items(self):
        return self._list_comments