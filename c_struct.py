from c_types import CVariable


class Cstruct():
    def __init__(self, struct_name: str, variables: list[CVariable]):
        self._name = struct_name
        self._variables = variables[:]

    def remove_by_variable_type(self, c_type: str):
        self._variables = [variable for variable in self._variables if variable.type != c_type]

    def replace_by_variable_type(self, c_type, new_types: list[CVariable]):
        self.remove_by_variable_type(c_type)
        for var in new_types:
            self._variables.append(var)

    def remove_by_variable_name(self, var_name):
        self._variables = [var for var in self._variables if var.name != var_name]

    def __str__(self):
        return f'{self.name} {self._variables}'

    @property
    def name(self):
        return self._name

    @property
    def variables(self):
        return self._variables

    @property
    def types(self):
        return [var.type for var in self._variables]


# x = Cstruct("test", [["uint8_t", "x"], ["uint32_t", "var"]])
# print(x.create_c_struct())
