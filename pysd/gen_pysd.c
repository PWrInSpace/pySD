#include <string.h>
#include "pysd/gen_pysd.h"

/**
 * @brief Get header size
 *
 * @param new_line_ending end string with new line character
 * @return size_t header size
 */
size_t pysd_get_header_size(bool new_line_ending) {
    size_t string_size;
    if (new_line_ending == true) {
        string_size = snprintf(NULL, 0, "x;k x;k z;\n");
    } else {
        string_size = snprintf(NULL, 0, "x;k x;k z;");
    }

    return string_size;
}

/**
 * @brief Get size of sd data frame
 *
 * @param pysd_main
 * @param new_line_ending end string with new line character
 * @return size_t frame size
 */
size_t pysd_get_sd_frame_size(kloc pysd_main, bool new_line_ending) {
    size_t string_size;
    if (new_line_ending == true) {
        string_size = snprintf(NULL, 0, "%d;%d;%f;\n", pysd_main.x, pysd_main.k.x, pysd_main.k.z);
    } else {
        string_size = snprintf(NULL, 0, "%d;%d;%f;", pysd_main.x, pysd_main.k.x, pysd_main.k.z);
    }

    return string_size;
}

/**
 * @brief Fill buffer with struct variables names
 * 
 * @param buffer pointer to buffer
 * @param size buffer size
 * @param kloc struct with data
 * @param new_line_ending end string with new line character
 * @return size_t size of wrote data, return 0 in case of failure
 */
size_t pysd_create_header(char *buffer, size_t size, bool new_line_ending) {
    size_t header_size;
    header_size = pysd_get_header_size(new_line_ending);

    if (header_size > size) {
        return false;
    }

    if (new_line_ending == true) {
        snprintf(buffer, size, "x;k x;k z;\n");
    } else {
        snprintf(buffer, size, "x;k x;k z;");
    }

    return header_size;
}

/**
 * @brief Fill buffer with struct data
 *
 * @param buffer pointer to buffer
 * @param size buffer size
 * @param ...pysd_main... struct with data
 * @param new_line_ending end string with new line character
 * @return size_t size of wrote data, return 0 in case of failure
 */
size_t pysd_create_sd_frame(char *buffer, size_t size, kloc pysd_main, bool new_line_ending) {
    size_t frame_size;
    frame_size = pysd_get_sd_frame_size(pysd_main, new_line_ending);

    if (frame_size > size) {
        return 0;
    }

    if (new_line_ending == true) {
        snprintf(buffer, size, "%d;%d;%f;\n", pysd_main.x, pysd_main.k.x, pysd_main.k.z);
    } else {
        snprintf(buffer, size, "%d;%d;%f;\n", pysd_main.x, pysd_main.k.x, pysd_main.k.z);
    }

    return frame_size;
}