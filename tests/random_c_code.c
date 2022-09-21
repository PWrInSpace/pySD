NVSResult NVS_init(void){
    esp_err_t res;

    res = nvs_flash_init();
    if(res != ESP_OK){
        ESP_LOGE(TAG, "NVS error init %s", esp_err_to_name(res));
        return NVS_INIT_ERROR;
    }

    nvs.handle = 0;
    return NVS_OK;
}

NVSResult NVS_write_uint8(const char* key, uint8_t val){
    esp_err_t res;
    res = nvs_open("storage", NVS_READWRITE, &nvs.handle);
    if(res != ESP_OK){
        ESP_LOGE(TAG, "NVS open error %s", esp_err_to_name(res));
        return NVS_OPEN_ERROR;
    }

    ESP_LOGI(TAG, "Writing to nvs %c", val);

    res = nvs_set_u8(nvs.handle, key, val);
    if(res != ESP_OK){
        nvs_close(nvs.handle);
        ESP_LOGE(TAG, "NVS write error %s", esp_err_to_name(res));
        return NVS_READ_ERROR;
    }

    nvs_close(nvs.handle);
    return NVS_OK;
}

NVSResult NVS_read_uint8(const char* key, uint8_t *val){
    esp_err_t res;
    res = nvs_open("storage", NVS_READONLY, &nvs.handle);
    if(res != ESP_OK){
        ESP_LOGE(TAG, "NVS open error %s", esp_err_to_name(res));
        return NVS_OPEN_ERROR;
    }

    res = nvs_get_u8(nvs.handle, key, val);
    if(res != ESP_OK){
        nvs_close(nvs.handle);
        ESP_LOGE(TAG, "NVS read error %s", esp_err_to_name(res));
        return NVS_READ_ERROR;
    }

    ESP_LOGI(TAG, "Read from nvs %c", *val);
    nvs_close(nvs.handle);
    return NVS_OK;
}