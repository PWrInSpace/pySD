#include <string.h>
#include "pysd/pysd.h"

void pysd_create_header(char *buffer, size_t size, pysdmain_dataframe pysd_main) {
    snprintf(buffer, size, "x;pitot z;pitot x;pitot a;pitot test;main_valve x;main_valve test;");
}


void pysd_create_sd_frame(char *buffer, size_t size, pysdmain_dataframe pysd_main) {
    snprintf(buffer, size, "%llu;%lu;%d;%f;%llu;%llu;%d;", pysd_main.x, pysd_main.pitot.z, pysd_main.pitot.x, pysd_main.pitot.a, pysd_main.pitot.test, pysd_main.main_valve.x, pysd_main.main_valve.test);
}