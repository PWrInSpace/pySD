from struct_reader import StructParser
class TestStructReader:
    def test_read_struct_from_file(self):
        name = "my_struct_t"
        variables = [["size_t", "z", None], 
                    ["uint8_t", "x", None], 
                    ["float", "a", None], 
                    ["uint64_t", "test", None]]
        sp = StructParser()
        sp.getVariablesFromFile("struct.c")

        assert name == sp.struct_name
        assert variables == sp.variable_list
