from config import DEFAULT_DIR_NAME
from struct_reader import StructReader
from struct_converter import StructConverter
from pysd_file_creator import PYSDFileCreator
import os


def main():
    read_struct = StructReader()
    read_struct.get_structs_from_file(os.getcwd() + "/struct.c")
    read_struct.check_prefixes()
    read_struct.add_user_structs_to_known_types()
    struct_converter = StructConverter(read_struct.structs_list)
    print(struct_converter.main_struct)

    file = PYSDFileCreator(
        struct_converter.main_struct,
        "struct.c",
        DEFAULT_DIR_NAME,
    )
    file.save_c_file(file.create_c_file())
    file.save_h_file(file.create_h_file())


if __name__ == "__main__":
    main()
