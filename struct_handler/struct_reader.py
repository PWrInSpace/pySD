import os
import json

types = {
    'int': 4,
    'float': 4,
    'double': 8,
    'char': 1,
    'uint8_t': 1,
    'uint16_t': 2,
    'uint32_t': 4,
    'uint64_t': 8,
    'int8_t': 1,
    'int16_t': 2,
    'int32_t': 4,
    'int64_t': 8,
}


keywords = ["const", "static", "volatile"]


class StructParser():
    def __init__(self):
        self._variables_list = []
        self._struct_name = None
        self._cwd = os.getcwd()
        self._types = self._readTypesFromJson()
        self._saved_structs = self._readStructsFromJson()

    def _readTypesFromJson(self):
        with open(self._cwd + "/jsons/types.json", "r") as json_file:
            return json.load(json_file)

    def _writeTypesToJson(self):
        with open(self._cwd + "/jsons/types.json", "w") as json_file:
            json_file.write(json.dumps(self.types, indent=4))

    def saveStructToJson(self,):
        if not self._variables_list:
            raise AttributeError("Struct is empty read")

        with open(self._cwd + "/jsons/structs.json", "w") as struct_file:
            struct_file.write(json.dumps(self._saved_structs, indent=4))

    def _readStructsFromJson(self):
        with open(self._cwd + "/jsons/structs.json", "r") as structs_file:
            return json.load(structs_file)

    def getVariablesFromFile(self, file_path) -> list:
        curly_brackets_open = 0
        curly_bracket_close = 0

        file = open(file_path, "r")
        for line in file:
            if '{' in line:
                curly_brackets_open += 1

            elif '}' in line:
                curly_bracket_close += 1
                if curly_bracket_close == curly_brackets_open and curly_brackets_open != 0:
                    line = line.replace('}', '').replace(';', '').replace('\n', '')
                    self._struct_name = line
                    return

            elif curly_brackets_open - curly_bracket_close == 1:
                line = line.replace('\n', '').replace(';', '').lstrip()
                var = line.split(' ')
                # keyword case
                if var[0] in keywords:
                    if len(var) > 4:  # packed case
                        self._variables_list.append([f'{var[0]} {var[1]}', var[2], var[4]])
                    else:
                        self._variables_list.append([var[0] + ' ' + var[1], var[2], None])
                # packed case
                elif len(var) > 3:
                    self._variables_list.append([var[0], var[1], var[3]])
                # default
                else:
                    self._variables_list.append([var[0], var[1], None])

    def checkTypesAndReturnUnknown(self):
        unknown_var_list = []
        var_types = [i[0] for i in self._variables_list]
        for name in var_types:
            # remove keyword
            if bool([word for word in keywords if (word in name)]):
                name = name.split(" ")[1]
            # check if name is in type_file
            if name not in types:
                unknown_var_list.append(name)

        return unknown_var_list

    def setNewType(self, name: str, size: str):
        self.types[name] = size
        self._writeTypesToJson()

    def removeType(self, name: str):
        if name in self._types.keys():
            del self._types[name]
            self._writeTypesToJson()
        else:
            raise ValueError("Unknown key")

    @property
    def variable_list(self):
        return self._variables_list

    @property
    def struct_name(self):
        return self._struct_name

    @property
    def types(self):
        return self._types

    @property
    def structs(self):
        return self._saved_structs


x = StructParser()
print(x.types)
print(x.structs)
x.getVariablesFromFile(os.getcwd() + "/struct.c")
print(x.variable_list)

# with open("structs.json", "r") as structs_file:
#             struct_list = json.load(structs_file)
#             print(struct_list[0][0])
#             # self._saved_structs = struct_list
