#include <stdint.h>
#include <stdio.h>
typedef struct{
    const size_t z;
    uint8_t x;
    float a;
}pysd_my_struct_t;


typedef struct{
    uint64_t x;
    pysd_my_struct_t test;
}pysd_test;

typedef struct{
    uint64_t x;
    int32_t test;
}pysdmain_dataframe;