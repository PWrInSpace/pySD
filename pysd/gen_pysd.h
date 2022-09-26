#ifndef PYSD_ZYGOCHUJ_H_
#define PYSD_ZYGOCHUJ_H_


#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "pysd_struct.h"

#ifdef __cplusplus
extern "C" {
#endif

size_t pysd_get_header_size(void);
size_t pysd_get_sd_frame_size(pysdmain_dataframe pysd_main);
bool pysd_create_header(char*buffer, size_t size, pysdmain_dataframe pysd_main);
bool pysd_create_sd_frame(char *buffer, size_t size, pysdmain_dataframe pysd_main);

#ifdef __cplusplus
}
#endif

#endif
