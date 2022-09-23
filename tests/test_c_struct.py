from c_struct import Cstruct
from c_types import CVariable
import pytest

types = [
    CVariable("uint8_t", "fish"),
    CVariable("int", "dog"),
    CVariable("float", "cat"),
    CVariable("int", "frog"),
]


@pytest.fixture()
def c_struct():
    return Cstruct("test_stuct", types)


def test_remove_types(c_struct):
    c_struct.remove_by_variable_type("int")
    new_types = []
    new_types.append(types[0])
    new_types.append(types[2])
    assert new_types == c_struct.variables


def test_remove_variable(c_struct):
    c_struct.remove_by_variable_type(types[0].type)
    new_types = types[:]
    del new_types[0]

    assert new_types == c_struct.variables
