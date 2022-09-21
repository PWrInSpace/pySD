import os
from c_struct import Cstruct

c_keywords = ["const", "static", "volatile"]
c_types = {
    'int',
    'float',
    'double',
    'char',
    'uint8_t',
    'uint16_t',
    'uint32_t',
    'uint64_t',
    'int8_t',
    'int16_t',
    'int32_t',
    'int64_t',
    'size_t',
    'unsigned int'
}

main_struct_prefix = "pysdmain"
sub_structs_prefix = "pysd"


class StructParser():
    def __init__(self):
        self.structs_list = []
        self._cwd = os.getcwd()

    def _check_is_struct_begin(self, line):
        return '{' in line and 'struct' in line

    def _check_is_struct_end(self, line):
        return '}' in line

    def get_structs_from_file(self, file_path) -> list:
        is_reading_struct = False
        types_buffer = []

        file = open(file_path, "r")
        for line in file:
            if self._check_is_struct_begin(line) is True:
                if is_reading_struct is True:
                    raise ValueError("Nested structs are not supported")

                is_reading_struct = True

            elif self._check_is_struct_end(line) is True and is_reading_struct is True:
                is_reading_struct = False
                name = line.replace('}', '').replace(';', '').replace('\n', '').strip()
                self.structs_list.append(Cstruct(name, types_buffer))
                types_buffer.clear()

            elif is_reading_struct is True:
                line = line.replace('\n', '').replace(';', '').lstrip()
                var = line.split(' ')
                # keyword case
                if var[0] == 'unsigned':
                    types_buffer([var[0] + ' ' + var[1], var[2]])
                elif var[0] in c_keywords:
                    types_buffer.append([var[1], var[2]])
                else:
                    types_buffer.append([var[0], var[1]])

        if len(self.structs_list) == 0:
            raise ValueError("File do not have structs")

    def check_prefixes(self):
        if False in [var.name.startswith(sub_structs_prefix) for var in self.structs_list]:
            raise ValueError("Struct do not have pysd prefix")

        if True not in [var.name.startswith(main_struct_prefix) for var in self.structs_list]:
            raise ValueError("Can't find struct with pysdmain prefix")

    @property
    def variable_list(self):
        return self.structs_list


def fnc():
    x = StructParser()
    x.get_structs_from_file(os.getcwd() + "/struct.c")
    print([i.__str__() for i in x.variable_list])
    x.check_prefixes()


if __name__ == '__main__':
    fnc()
