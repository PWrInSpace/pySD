from struct_reader import StructReader
from struct_converter import StructConverter
# from pysd_file_creator import PYSDFileCreator
import os


def main():
    read_struct = StructReader()
    read_struct.get_structs_from_file(os.getcwd() + "/struct.c")
    read_struct.check_prefixes()
    read_struct.add_user_structs_to_known_types()
    struct_converter = StructConverter(read_struct.structs_list)
    print(struct_converter.main_struct)

    # file = PYSDFileCreator("pysd_generator", "XDDD", struct_converter.main_struct)
    # file.configure_h_file()


if __name__ == "__main__":
    main()
