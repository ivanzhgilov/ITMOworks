# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

class DuplicateKeyError(Exception):
    def __init__(self, source, key, number_line, section_name):
        self.key = key
        self.section_name = section_name
        self.number_line = number_line
        self.source = source

    def __str__(self):
        return "While reading from '{}' [line {}]: key '{}' in section '{}' already exists".format(self.source,
                                                                                                   self.number_line,
                                                                                                   self.key,
                                                                                                   self.section_name)


class DuplicateSectionError(Exception):
    def __init__(self, source, number_line, section_name):
        self.source = source
        self.number_line = number_line
        self.section_name = section_name

    def __str__(self):
        return "While reading from '{}' [line  {}]: section '{}' already exists".format(self.source,
                                                                                        self.number_line,
                                                                                        self.section_name)


class MissingSectionHeaderError(Exception):
    def __init__(self, source, number_line):
        self.source = source
        self.number_line = number_line

    def __str__(self):
        return "File '{}' [line {}] contains no section headers.".format(self.source, self.number_line)


class ParsingError(Exception):
    def __init__(self, source, number_line, string):
        self.source = source
        self.number_line = number_line
        self.string = string

    def __str__(self):
        return "Source contains parsing errors: '{}' [line {}]: {}".format(self.source,
                                                                           self.number_line,
                                                                           self.string)

class NoSectionError(Exception):
    def __init__(self, section_name):
        self.section_name = section_name

    def __str__(self):
        return "No section: '{}'".format(self.section_name)

class NoKeyError(Exception):
    def __init__(self, section_name, key):
        self.section_name = section_name
        self.key = key

    def __str__(self):
        return "No key: '{}' in section: '{}'".format(self.key, self.section_name)