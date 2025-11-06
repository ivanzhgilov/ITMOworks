# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

from classes.binary_parser import BinaryParser
from classes.ini_parser import INIParser
from classes.section_classes import Comments


def complete_base_task(filename_ini, filename_bin):
    ini_parser = INIParser()
    binary_parser = BinaryParser()

    ini_parser.read(filename_ini)
    data = ini_parser.get_all_sections()
    comments = ini_parser.get_all_comments()

    binary_parser.save_to_file(filename_bin, data, comments)

if __name__ == "__main__":
    complete_base_task("../data/schedule.ini", "../data/schedule.bin")
