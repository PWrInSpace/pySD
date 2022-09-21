

class Cstruct():
    def __init__(self, name: str, var: list):
        self.name = name
        self.variables_list = var

    def struct_to_list(self) -> list:
        return [self.name, self.variables_list]

    def create_c_struct(self) -> str:
        c_struct = "typedef struct {\n"
        for var in self.variables_list:
            c_struct += "   {} {};\n".format(var[0], var[1])
        c_struct += "} " + "{};".format(self.name)
        return c_struct


x = Cstruct("test", [["uint8_t", "x"], ["uint32_t", "var"]])
print(x.create_c_struct())
