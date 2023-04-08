import os
from c_struct import Cstruct
from c_types import CVariable
from config import C_KEYWORDS, C_TYPES, MAIN_STRUCT_PREFIX, SUB_STRUCTS_PREFIX


class StructReader():
    def __init__(self):
        self._structs_list: list[Cstruct] = []

    def _check_is_struct_begin(self, line):
        return '{' in line and 'struct' in line

    def _check_is_struct_end(self, line):
        return '}' in line

    def get_structs_from_file(self, file_path) -> list:
        is_reading_struct = False
        variables_buffer = []

        file = open(file_path, "r")
        for line in file:
            if self._check_is_struct_begin(line) is True:
                if is_reading_struct is True:
                    raise ValueError("Nested structs are not supported")

                is_reading_struct = True

            elif self._check_is_struct_end(line) is True and is_reading_struct is True:
                is_reading_struct = False
                name = line.replace('}', '').replace(';', '').replace('\n', '').strip()
                self._structs_list.append(Cstruct(name, variables_buffer, file_path))
                variables_buffer.clear()

            elif is_reading_struct is True:
                line = line.replace('\n', '').replace(';', '').lstrip()
                var = line.split(' ')
                if var[0] == 'unsigned':
                    variables_buffer([])
                    variables_buffer.append(CVariable(var[0] + ' ' + var[1], var[2]))
                elif var[0] in C_KEYWORDS:
                    variables_buffer.append(CVariable(var[1], var[2]))
                else:
                    if var[0] != "":
                        variables_buffer.append(CVariable(var[0], var[1]))


    def _contains_struct_without_prefix(self):
        return False in [
            struct.name.startswith(SUB_STRUCTS_PREFIX) for struct in self._structs_list
        ]

    def _do_not_contains_struct_with_main_prefix(self):
        return True not in [var.name.startswith(MAIN_STRUCT_PREFIX) for var in self._structs_list]

    def check_prefixes(self):
        if self._contains_struct_without_prefix() is True:
            raise ValueError("Struct do not have pysd prefix")

        if self._do_not_contains_struct_with_main_prefix() is True:
            raise ValueError("Can't find struct with pysdmain prefix")

    def add_user_structs_to_known_types(self):
        for struct in self._structs_list:
            C_TYPES.append(struct.name)

    def check_types_in_structs(self):
        types_in_structs = []
        for struct in self._structs_list:
            types_in_structs += struct.types

        for variable_type in types_in_structs:
            if variable_type not in C_TYPES:
                raise ValueError(f'Type {variable_type} is unknown :C')

    @property
    def structs_list(self):
        return self._structs_list


def fnc():
    x = StructReader()
    x.get_structs_from_file(os.getcwd() + "/struct.c")
    x.check_prefixes()
    x.check_types_in_structs()


if __name__ == '__main__':
    fnc()
