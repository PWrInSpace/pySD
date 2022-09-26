#ifndef PYSD_ZYGOCHUJ_H_
#define PYSD_ZYGOCHUJ_H_


#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "struct.c"

#ifdef __cplusplus
extern "C" {
#endif

void pysd_create_header(char*buffer, size_t size, pysdmain_dataframe pysd_main);
void pysd_create_sd_frame(char *buffer, size_t size, pysdmain_dataframe pysd_main);

#ifdef __cplusplus
}
#endif

#endif
