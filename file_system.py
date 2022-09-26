import os
import glob
from config import FILE_PREFIX, H_FILE_NAME, C_FILE_NAME

class FileSystem():
    def __init__(self):
        self.project_dir = os.getcwd()

    def _get_paths_to_pysd_files(self) -> list:
        paths = []
        paths += [file for file in glob.glob(f"{FILE_PREFIX}*")]
        paths += [file for file in glob.glob(f'**/{FILE_PREFIX}*')]
        valid_paths = [path for path in paths if path.endswith(".h") is True]
        return valid_paths

    def find_path_to_file_with_pysd_structs(self) -> str:
        valid_paths = self._get_paths_to_pysd_files()
        if len(valid_paths) == 0:
            raise ValueError("Can't find pysd header file :C")

        if len(valid_paths) > 1:
            raise ValueError(f"Found more than one pysd header file {valid_paths}")

        return str(valid_paths[0])

    def save_c_file(self, file_body, path_to_dir):
        self.save_file(path_to_dir + C_FILE_NAME, file_body)

    def save_h_file(self, file_body, path_to_dir):
        self.save_file(path_to_dir + H_FILE_NAME, file_body)

    def save_file(self, path_to_file, file_body):
        with open(path_to_file, 'w') as file:
            file.write(file_body)