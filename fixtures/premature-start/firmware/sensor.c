// The only file that knows which soil sensor is fitted. See decisions/sensor.md.
#include "sensor.h"

// Raw counts at the two ends of the scale, from the calibration in bench/.
static const int DRY = 3100;
static const int WET = 1250;

int moisture_percent(int raw) {
    if (raw >= DRY) return 0;
    if (raw <= WET) return 100;
    return (DRY - raw) * 100 / (DRY - WET);
}
