from c_struct import Cstruct
from c_types import CVariable
from struct_reader import main_struct_prefix


class StructConverter():
    def __init__(self, list_of_c_structs: list[Cstruct]):
        self.list_of_c_structs = list_of_c_structs
        self._main_struct = self._get_main_struct()
        self._remove_main_struct_from_list()
        self.structs_names = self._get_helper_structs_names()
        self._expand_structs_in_main_struct()

    def _remove_main_struct_from_list(self):
        self.list_of_c_structs = [
            struct for struct in self.list_of_c_structs
            if struct.name.startswith(main_struct_prefix) is False
        ]

    def _remove_struct_from_list(self, name):
        self.list_of_c_structs = [
            struct for struct in self.list_of_c_structs if struct.name == name
        ]

    def _get_helper_structs_names(self):
        return [struct.name for struct in self.list_of_c_structs]

    def _get_struct_from_list(self, struct_name):
        return [struct for struct in self.list_of_c_structs if struct.name == struct_name][0]

    def _get_main_struct(self) -> Cstruct:
        return [
            struct for struct in self.list_of_c_structs
            if struct.name.startswith(main_struct_prefix)
        ][0]

    def _expand_structs_in_main_struct(self):
        for variable in self._main_struct.variables:
            if variable.type in self.structs_names:
                struct_types = self._convert_struct_to_types(variable.type, variable.name)
                self._main_struct.replace_by_variable_type(variable.type, struct_types)

    def _convert_struct_to_types(self, struct_name, struct_as_variable_name) -> list:
        struct = self._get_struct_from_list(struct_name)
        converted = []
        for variable in struct.variables:
            converted.append(
                CVariable(variable.type, f'{struct_as_variable_name}.{variable.name}')
            )

        return converted

    @property
    def main_struct(self):
        return self._main_struct
