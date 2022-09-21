

class Cstruct():
    def __init__(self, name: str, var: list):
        self._name = name
        self._types_list = var[:]

    def struct_to_list(self) -> list:
        return [self.name, self.types_list]

    def create_c_struct(self) -> str:
        c_struct = "typedef struct {\n"
        for var in self.types_list:
            c_struct += "   {} {};\n".format(var[0], var[1])
        c_struct += "} " + "{};".format(self.name)
        return c_struct

    def __str__(self):
        return f'{self.name} {self.types_list.__str__()}'

    @property
    def name(self):
        return self._name

    @property
    def types_list(self):
        return self._types_list


# x = Cstruct("test", [["uint8_t", "x"], ["uint32_t", "var"]])
# print(x.create_c_struct())
