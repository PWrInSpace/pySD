#ifndef PYSD_ZYGOCHUJ_H_
#define PYSD_ZYGOCHUJ_H_


#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include "/home/kuba/pwrinspace/git/pySD/tests/test.h"

#ifdef __cplusplus
extern "C" {
#endif

size_t pysd_get_header_size(bool new_line_ending);
size_t pysd_get_sd_frame_size(kloc pysd_main, bool new_line_ending);
size_t pysd_create_header(char*buffer, size_t size, bool new_line_ending);
size_t pysd_create_sd_frame(char *buffer, size_t size, kloc pysd_main, bool new_line_ending);

#ifdef __cplusplus
}
#endif

#endif
