# Author = Zhgilev Ivan Igorevich
# Group = P3130
# Date = 01.11.2025
# Variant 86
import timeit

from classes.binary_parser import BinaryParser
from classes.xml_serializer import XMLSerializer

def complete_additional_task_3(filename_bin="../data/schedule.bin", filename_xml="../data/schedule.xml"):
    binary_parser = BinaryParser()
    xml_serializer = XMLSerializer()

    data = binary_parser.load_from_file(filename_bin)

    xml_serializer.save_to_file(data, filename_xml)


if __name__ == "__main__":
    complete_additional_task_3("../data/schedule.bin", "../data/schedule.xml")
