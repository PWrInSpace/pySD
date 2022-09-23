H_FILE_NAME = "/zygochuj.h.pysd"
C_FILE_NAME = "/zygochuj.c.pysd"
PYSD_STRUCT_ID = "...pysd_main_name..."
PYSD_INCLUDE_PATH_TO_DEF_ID = "...include_to_def..."


class PYSDFileCreator():

    def __init__(self, path_to_template, path_to_save, pysdmain_struct) -> None:
        self.path_to_template_dir = path_to_template
        self.path_to_save = path_to_save
        self.main_struct = pysdmain_struct

    def _get_template_body(self, file_path):
        with open(file_path, "r") as template:
            return template.read()

    def configure_h_file(self):
        file_body = self._get_template_body(self.path_to_template_dir + H_FILE_NAME)
        file_body = self.set_pysd_struct(file_body)
        file_body = self.set_include_path(file_body, "1234TEST")
        print(file_body)

    def set_pysd_struct(self, file_body):
        return file_body.replace(PYSD_STRUCT_ID, self.main_struct.name)

    def set_include_path(self, file_body, path_to_pysd_file_def):
        return file_body.replace(PYSD_INCLUDE_PATH_TO_DEF_ID, path_to_pysd_file_def)
