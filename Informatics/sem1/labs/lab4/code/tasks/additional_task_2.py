# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

import timeit
import datetime

from classes.library_converter import LibraryConverter


def complete_additional_task_2(filename_ini="../data_lib/schedule.ini", filename_bin="../data_lib/schedule_lib.bin",
                               filename_hcl="../data_lib/schedule_lib.hcl"):
    converter = LibraryConverter()

    converter.ini_to_bin_library(filename_ini, filename_bin)

    converter.bin_to_hcl_library(filename_bin, filename_hcl)


if __name__ == "__main__":
    complete_additional_task_2("../data_lib/schedule.ini", "../data_lib/schedule_lib.bin",
                               "../data_lib/schedule_lib.hcl")

