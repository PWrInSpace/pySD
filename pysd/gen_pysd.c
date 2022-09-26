#include <string.h>
#include "pysd/gen_pysd.h"

size_t pysd_get_header_size(void) {
    return sprintf(NULL, "x;pitot z;pitot x;pitot a;pitot test;main_valve x;main_valve test;upust_valve dog;upust_valve cat;");
}


size_t pysd_get_sd_frame_size(pysdmain_dataframe pysd_main) {
    return sprintf(NULL, "%llu;%lu;%d;%f;%llu;%llu;%d;%d;%f;", pysd_main.x, pysd_main.pitot.z, pysd_main.pitot.x, pysd_main.pitot.a, pysd_main.pitot.test, pysd_main.main_valve.x, pysd_main.main_valve.test, pysd_main.upust_valve.dog, pysd_main.upust_valve.cat);
}

bool pysd_create_header(char *buffer, size_t size, pysdmain_dataframe pysd_main) {
    size_t header_size;
    header_size = pysd_get_header_size();

    if (header_size > size) {
        return false;
    }

    snprintf(buffer, size, "x;pitot z;pitot x;pitot a;pitot test;main_valve x;main_valve test;upust_valve dog;upust_valve cat;");

    return true;
}


bool pysd_create_sd_frame(char *buffer, size_t size, pysdmain_dataframe pysd_main) {
    size_t frame_size;
    frame_size = pysd_get_sd_frame_size(pysd_main);

    if (frame_size > size) {
        return false;
    }

    snprintf(buffer, size, "%llu;%lu;%d;%f;%llu;%llu;%d;%d;%f;", pysd_main.x, pysd_main.pitot.z, pysd_main.pitot.x, pysd_main.pitot.a, pysd_main.pitot.test, pysd_main.main_valve.x, pysd_main.main_valve.test, pysd_main.upust_valve.dog, pysd_main.upust_valve.cat);

    return true;
}