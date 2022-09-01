#include <stdint.h>
#include <stdio.h>

typedef struct{
    const size_t z;
    uint8_t x;
    float a;
    volatile uint64_t test : 5;
}my_struct_t;
