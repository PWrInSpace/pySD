#include <stdint.h>
#include <stdio.h>

typedef struct{
    const size_t z;
    uint8_t x;
    float a;
    uint64_t test;
}pysd_pitot;


typedef struct{
    uint64_t x;
    int32_t test;
}pysd_main_valve;

typedef struct{
    uint64_t x;
    pysd_pitot pitot;
    pysd_main_valve main_valve;
}pysdmain_dataframe;