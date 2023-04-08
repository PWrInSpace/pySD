import sys
from struct_reader import StructReader
from struct_converter import StructConverter
from pysd_file_creator import PYSDFileCreator
from file_system import FileSystem
from config import DEFAULT_DIR_NAME, bcolors

from pathlib import Path
import os


STARTUP_FLAGS = {
    '-d': FileSystem.set_path_to_both_file_output,
    '-dc': FileSystem.set_path_to_c_file_output,
    '-dh': FileSystem.set_path_to_h_file_output,
    '-s': FileSystem.set_struct,
}


def startup_flags_check():
    arguments = sys.argv[1:]
    arg_pos = 0
    while arg_pos < len(arguments):
        arg = arguments[arg_pos]
        if arg in STARTUP_FLAGS:
            arg_pos += 1
            STARTUP_FLAGS[arg](arguments[arg_pos])
        else:
            raise ValueError(f"Unknonw flag {arg}")
        arg_pos += 1


def get_paths_to_c_files(dir = "") -> list[str]:
    paths = [str(file) for file in Path(dir).rglob("*.h")]
    return paths

def expand_struct(list_of_structs, struct_name):
    struct = [struct for struct in list_of_structs if struct.name == struct_name][0]
    print(struct)
    for var in struct.variables:
        if var.type in [x.name for x in list_of_structs]:
            struct.remove_by_variable_type(var.type)
            print(var)

def main():
    startup_flags_check()
    reader = StructReader()
    paths = get_paths_to_c_files(os.getcwd())
    for path in paths:
        reader.get_structs_from_file(path)

    conv = StructConverter(reader.structs_list, FileSystem.STRUCT)
    print(f"{bcolors.OKCYAN}{conv.main_struct}{bcolors.OKCYAN}")
    file_system = FileSystem()


    # pysd_file_path = file_system.find_path_to_file_with_pysd_structs()
    # read_struct = StructReader()
    # read_struct.get_structs_from_file(pysd_file_path)
    # read_struct.check_prefixes()
    # # read_struct.add_user_structs_to_known_types()
    # struct_converter = StructConverter(read_struct.structs_list)

    file = PYSDFileCreator(
        conv.main_struct,
        conv.main_struct.path,
        DEFAULT_DIR_NAME,
    )

    if file_system.check_if_save_dir_exist() is False:
        file_system.create_directory()

    c_file_template = file_system.get_c_template_from_file()
    file_system.save_c_file(file.create_c_file(c_file_template))
    h_file_template = file_system.get_h_template_from_file()
    file_system.save_h_file(file.create_h_file(h_file_template))

    print(f"{bcolors.OKGREEN}pysd files created at {DEFAULT_DIR_NAME} directory :){bcolors.ENDC}")


if __name__ == "__main__":
    main()
