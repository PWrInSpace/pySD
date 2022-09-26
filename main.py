from struct_reader import StructReader
from struct_converter import StructConverter
from pysd_file_creator import PYSDFileCreator
from file_system import FileSystem
from config import DEFAULT_DIR_NAME


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    file_system = FileSystem()
    pysd_file_path = file_system.find_path_to_file_with_pysd_structs()
    read_struct = StructReader()
    read_struct.get_structs_from_file(pysd_file_path)
    read_struct.check_prefixes()
    read_struct.add_user_structs_to_known_types()
    struct_converter = StructConverter(read_struct.structs_list)

    file = PYSDFileCreator(
        struct_converter.main_struct,
        pysd_file_path,
        DEFAULT_DIR_NAME,
    )

    if file_system.check_if_save_dir_exist(DEFAULT_DIR_NAME) is False:
        file_system.create_directory(DEFAULT_DIR_NAME)

    c_file_template = file_system.get_c_template_from_file()
    file_system.save_c_file(file.create_c_file(c_file_template), DEFAULT_DIR_NAME)
    h_file_template = file_system.get_h_template_from_file()
    file_system.save_h_file(file.create_h_file(h_file_template), DEFAULT_DIR_NAME)

    print(f"{bcolors.OKGREEN}pysd files created at {DEFAULT_DIR_NAME} directory :){bcolors.ENDC}")


if __name__ == "__main__":
    main()
