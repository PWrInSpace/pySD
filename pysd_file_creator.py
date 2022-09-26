from c_struct import Cstruct
from config import C_FILE_NAME, H_FILE_NAME, TYPE_TO_SPECIFIER

PATH_TO_H_FILE_TEMPLATE = "pysd_templates/zygochuj.h.pysd"
PATH_TO_C_FILE_TEMPLATE = "pysd_templates/zygochuj.c.pysd"
PYSD_STRUCT_ID = "...pysd_main_name..."
PYSD_INCLUDE_PATH_TO_DEF_ID = "...include_to_def..."
PYSD_SPECIFIER_ID = "...sd_frame_specifier..."
PYSD_SD_FRAME_VARIABLES_ID = "...sd_frame_variables..."
PYSD_HEADER_TEXT_ID = "...header_text..."
PYSD_INCLUDE_H_PATH = "...pysd_h_include..."
PYSD_STRUCT_ARG_NAME = "pysd_main"


class PYSDFileCreator():

    def __init__(self, pysdmain_struct: Cstruct, path_to_user_structs, path_to_save) -> None:
        self.main_struct = pysdmain_struct
        self.path_to_user_structs = path_to_user_structs
        self.path_to_save = path_to_save

    def _get_template_body(self, file_path):
        with open(file_path, "r") as template:
            return template.read()

    def create_h_file(self):
        file_body = self._get_template_body(PATH_TO_H_FILE_TEMPLATE)
        file_body = self._set_pysd_main_struct(file_body)
        file_body = self._set_user_struct_include_path(file_body, self.path_to_user_structs)
        return file_body

    def _set_pysd_main_struct(self, file_body):
        return file_body.replace(PYSD_STRUCT_ID, self.main_struct.name)

    def _set_user_struct_include_path(self, file_body, user_struct_include_path):
        return file_body.replace(PYSD_INCLUDE_PATH_TO_DEF_ID, user_struct_include_path)

    def create_c_file(self):
        file_body = self._get_template_body(PATH_TO_C_FILE_TEMPLATE)
        file_body = self._set_pysd_main_struct(file_body)
        file_body = self._set_sprintf_specifier(file_body)
        file_body = self._set_sd_frame_variables(file_body)
        file_body = self._set_header_text(file_body)
        file_body = self._set_pysd_include_path(file_body)
        return file_body

    def _create_specifier(self):
        specifier_text = ""
        for variable in self.main_struct.variables:
            specifier_text += f"{TYPE_TO_SPECIFIER[variable.type]};"

        specifier_text = f'"{specifier_text}"'
        return specifier_text

    def _set_sprintf_specifier(self, file_body):
        specifier_text = self._create_specifier()
        return file_body.replace(PYSD_SPECIFIER_ID, specifier_text)

    def _create_sd_frame_variables(self):
        frame_variables = ""
        for variable in self.main_struct.variables:
            frame_variables += f'{PYSD_STRUCT_ARG_NAME}.{variable.name}, '
        return frame_variables[:-2]

    def _set_sd_frame_variables(self, file_body):
        variables = self._create_sd_frame_variables()
        return file_body.replace(PYSD_SD_FRAME_VARIABLES_ID, variables)

    def _create_header_text(self):
        header_text = ""
        for variable in self.main_struct.variables:
            header_text += f'{variable.name.replace(".", " ")};'

        return f'"{header_text}"'

    def _set_header_text(self, file_body):
        header_text = self._create_header_text()
        return file_body.replace(PYSD_HEADER_TEXT_ID, header_text)

    def _set_pysd_include_path(self, file_body):
        return file_body.replace(PYSD_INCLUDE_H_PATH, self.path_to_save + H_FILE_NAME)
