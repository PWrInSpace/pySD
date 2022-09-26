import os
from pathlib import Path
from config import FILE_PREFIX, H_FILE_NAME, C_FILE_NAME, TEMPLATE_C_PATH,\
                    TEMPLATE_H_PATH, DEFAULT_DIR_NAME


class FileSystem():
    OUTPUT_DIR_C_FILE = DEFAULT_DIR_NAME
    OUTPUT_DIR_H_FILE = DEFAULT_DIR_NAME

    def __init__(self):
        self.program_dir = os.getcwd()
        os.chdir("..")
        self.project_dir = os.getcwd()

    @classmethod
    def set_path_to_h_file_output(self, output_dir):
        self.OUTPUT_DIR_H_FILE = output_dir + "/pysd/"

    @classmethod
    def set_path_to_c_file_output(self, output_dir):
        self.OUTPUT_DIR_C_FILE = output_dir + "/pysd/"

    @classmethod
    def set_path_to_both_file_output(self, output_dir):
        self.set_path_to_c_file_output(output_dir)
        self.set_path_to_h_file_output(output_dir)

    def _get_paths_to_pysd_files(self) -> list:
        paths = []
        paths += [str(file) for file in Path(self.project_dir).rglob(f'{FILE_PREFIX}*')]
        print(paths)
        valid_paths = [path for path in paths if path.endswith(".h") is True]
        return valid_paths

    def find_path_to_file_with_pysd_structs(self) -> str:
        valid_paths = self._get_paths_to_pysd_files()
        if len(valid_paths) == 0:
            raise ValueError("Can't find pysd header file :C")

        if len(valid_paths) > 1:
            raise ValueError(f"Found more than one pysd header file {valid_paths}")

        return str(valid_paths[0])

    def save_c_file(self, file_body):
        self.save_file(self.OUTPUT_DIR_C_FILE + C_FILE_NAME, file_body)

    def save_h_file(self, file_body):
        self.save_file(self.OUTPUT_DIR_H_FILE + H_FILE_NAME, file_body)

    def save_file(self, path_to_file, file_body):
        with open(path_to_file, 'w') as file:
            file.write(file_body)

    def get_c_template_from_file(self):
        return self.read_from_file(self.program_dir + TEMPLATE_C_PATH)

    def get_h_template_from_file(self):
        return self.read_from_file(self.program_dir + TEMPLATE_H_PATH)

    def read_from_file(self, file_path):
        with open(file_path, "r") as template:
            return template.read()

    def check_if_save_dir_exist(self):
        return os.path.isdir(self.OUTPUT_DIR_C_FILE) and os.path.isdir(self.OUTPUT_DIR_H_FILE)

    def create_directory(self):
        os.mkdir(self.OUTPUT_DIR_H_FILE)
        os.mkdir(self.OUTPUT_DIR_C_FILE)
