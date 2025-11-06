# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86

from classes.binary_parser import BinaryParser
from classes.hcl_serializer import HCLSerializer

def complete_additional_task_1(filename_bin, filename_hcl):
    binary_parser = BinaryParser()
    hcl_serializer = HCLSerializer()

    data = binary_parser.load_from_file(filename_bin)

    hcl_serializer.save_to_file(data, filename_hcl)

if __name__ == "__main__":
    complete_additional_task_1("../data/schedule.bin", "../data/schedule.hcl")