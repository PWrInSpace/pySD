TYPE_TO_SPECIFIER = {
    'int': "%d",
    'float': "%f",
    'double': "%f",
    'char': "%c",
    'uint8_t': "%d",
    'uint16_t': "%d",
    'uint32_t': "%lu",
    'uint64_t': "%llu",
    'int8_t': "%c",
    'int16_t': "%d",
    'int32_t': "%d",
    'int64_t': "%d",
    'size_t': "%lu",
    'unsigned int': "%lu",
}

C_TYPES = list(TYPE_TO_SPECIFIER.keys())
C_KEYWORDS = ["const", "static", "volatile"]

FILE_PREFIX = "pysd"

MAIN_STRUCT_PREFIX = "pysdmain"
SUB_STRUCTS_PREFIX = "pysd"

C_FILE_NAME = "gen_pysd.c"
H_FILE_NAME = "gen_pysd.h"
DEFAULT_DIR_NAME = "pysd/"
