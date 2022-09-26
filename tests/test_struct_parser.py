import pytest
import os
from c_types import CVariable
from struct_reader import StructReader
from c_struct import Cstruct

VALID_STRUCT_PATH = "/tests/valid_struct.c"
STRUCT_WITHOUT_PREFIX = '/tests/without_prefix.c'
STRUCT_WITHOUT_MAIN_PREFIX = "/tests/without_main_prefix.c"
EMPTY_FILE = "/tests/empty_file.c"
RANDOM_CODE_WITHOUT_STRUCT = "/tests/random_c_code.c"
NESTED_STRUCT = "/tests/nested_struct.c"
STRUCT_WITH_UNKNOWN_TYPE = "/tests/struct_with_unknown_type.c"


@pytest.fixture
def parser():
    return StructReader()


@pytest.fixture
def c_struct_list_from_valid_struct():
    c_struct_list = []
    var = Cstruct(
        "pysd_my_struct_t",
        [
            CVariable('size_t', 'z'),
            CVariable('uint8_t', 'x'),
            CVariable('float', 'a')
        ])
    c_struct_list.append(var)

    var = Cstruct(
        "pysd_test",
        [
            CVariable('uint64_t', 'x'),
            CVariable('pysd_my_struct_t', 'test')
        ])
    c_struct_list.append(var)

    var = Cstruct(
        "pysdmain_dataframe",
        [
            CVariable('uint64_t', 'x'),
            CVariable('int32_t', 'test')
        ])
    c_struct_list.append(var)
    return c_struct_list


def test_get_structs_from_file(parser, c_struct_list_from_valid_struct):
    parser.get_structs_from_file(os.getcwd() + VALID_STRUCT_PATH)
    acctual_names = [var.name for var in parser.structs_list]
    acctual_variables = [var.types for var in parser.structs_list]
    expect_names = [var.name for var in c_struct_list_from_valid_struct]
    expect_variables = [var.types for var in c_struct_list_from_valid_struct]

    assert expect_names == acctual_names
    assert expect_variables == acctual_variables


def test_pass_file_without_struct(parser):
    with pytest.raises(ValueError):
        parser.get_structs_from_file(os.getcwd() + NESTED_STRUCT)
    with pytest.raises(ValueError):
        parser.get_structs_from_file(os.getcwd() + EMPTY_FILE)

    with pytest.raises(ValueError):
        parser.get_structs_from_file(os.getcwd() + RANDOM_CODE_WITHOUT_STRUCT)


def test_check_prefixes(parser):
    parser.get_structs_from_file(os.getcwd() + VALID_STRUCT_PATH)
    try:
        parser.check_prefixes()
    except ValueError:
        pytest.fail("Unexpected MyError ..")

    parser.get_structs_from_file(os.getcwd() + STRUCT_WITHOUT_PREFIX)
    with pytest.raises(ValueError):
        parser.check_prefixes()

    parser.get_structs_from_file(os.getcwd() + STRUCT_WITHOUT_MAIN_PREFIX)
    with pytest.raises(ValueError):
        parser.check_prefixes()


def test_check_types_in_struct(parser):
    parser.get_structs_from_file(os.getcwd() + STRUCT_WITHOUT_PREFIX)
    try:
        parser.check_types_in_structs()
    except ValueError:
        pytest.fail("Unexpected MyError ..")

    parser.get_structs_from_file(os.getcwd() + VALID_STRUCT_PATH)
    with pytest.raises(ValueError):
        parser.check_types_in_structs()

    parser.add_user_structs_to_known_types()
    try:
        parser.check_types_in_structs()
    except ValueError:
        pytest.fail("Unexpected MyError ..")

    parser.get_structs_from_file(os.getcwd() + STRUCT_WITH_UNKNOWN_TYPE)
    with pytest.raises(ValueError):
        parser.check_types_in_structs()
