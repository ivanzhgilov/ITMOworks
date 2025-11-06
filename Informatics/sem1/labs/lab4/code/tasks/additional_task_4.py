# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

import timeit

from base_task import complete_base_task
from additional_task_1 import complete_additional_task_1
from additional_task_2 import complete_additional_task_2

def manual_converter():
    filename_ini = "../data_test_time/schedule.ini"
    filename_bin = "../data_test_time/schedule_man.bin"
    filename_hcl = "../data_test_time/schedule_man.hcl"
    complete_base_task(filename_ini, filename_bin)
    complete_additional_task_1(filename_bin, filename_hcl)

def lib_converter():
    filename_ini = "../data_test_time/schedule.ini"
    filename_bin = "../data_test_time/schedule_lib.bin"
    filename_hcl = "../data_test_time/schedule_lib.hcl"
    complete_additional_task_2(filename_ini, filename_bin, filename_hcl)


if __name__ == "__main__":
    time_man = timeit.timeit(manual_converter, number=100)
    time_lib = timeit.timeit(lib_converter, number=100)

    print("{} seconds - base_task + additional_task_1".format(time_man))
    print("{} seconds - additional_task_2".format(time_lib))