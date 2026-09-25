// SoilSense firmware configuration
#pragma once

#define READ_INTERVAL_S      10      // send a reading every 10 seconds
#define WIFI_TX_CURRENT_MA   160     // ESP32 datasheet: Wi-Fi transmit, typical
#define WIFI_ON_TIME_S       3       // wake, connect and post, timed on the bench
#define SLEEP_CURRENT_MA     0.01    // ESP32 datasheet: deep sleep
#define BATTERY_MAH          2500    // two AA alkaline cells

#define GROWCLOUD_URL        "https://api.growcloud.example/v1/readings"
