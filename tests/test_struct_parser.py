import pytest
import os
from struct_handler.struct_reader import StructParser

STRUCT_PATH = "/tests/test_struct.c"

class TestStructReader:
    def test_read_struct_from_file(self):
        name = "my_struct_t"
        variables = [["const size_t", "z", None], 
                    ["uint8_t", "x", None], 
                    ["float", "a", None], 
                    ["volatile uint64_t", "test", "5"]]
        sp = StructParser()
        sp.getVariablesFromFile(os.getcwd() + STRUCT_PATH)

        assert name == sp.struct_name
        assert variables == sp.variable_list

    def test_pass_unknown_file(slef):
        sp = StructParser()

        with pytest.raises(FileNotFoundError):
            sp.getVariablesFromFile("test.xddd")

    def test_return_unknown_types(self):
        corrcet_unknown_list = ["size_t"]
        sp = StructParser()
        sp.getVariablesFromFile(os.getcwd() + STRUCT_PATH)
        unknown = sp.checkTypesAndReturnUnknown()
        
        assert unknown == corrcet_unknown_list
