# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

# noinspection PyCompatibility
import configparser
import pickle
import hcl2
import datetime


class LibraryConverter:

    def ini_to_bin_library(self, ini_file, bin_file):
        config = configparser.ConfigParser()
        config.read(ini_file, encoding='utf-8')

        data_dict = {}
        for section in config.sections():
            data_dict[section] = dict(config.items(section))

        with open(bin_file, 'wb') as f:
            pickle.dump(data_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

    def bin_to_hcl_library(self, bin_file, hcl_file):
        """Конвертация BIN -> HCL с использованием библиотеки hcl2"""

        # Десериализация из бинарного формата
        with open(bin_file, 'rb') as f:
            data_dict = pickle.load(f)

        hcl_structure = hcl2.reverse_transform(data_dict)

        hcl_content = hcl2.writes(hcl_structure)

        with open(hcl_file, 'w', encoding='utf-8') as f:
            f.write(hcl_content)


if __name__ == "__main__":
    converter = LibraryConverter()
    converter.ini_to_bin_library("../data_lib/schedule.ini", "../data_lib/schedule_lib.bin")
    converter.bin_to_hcl_library("../data_lib/schedule_lib.bin", "../data_lib/schedule_lib.hcl")
