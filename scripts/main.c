#include <stdio.h>
#include <stdlib.h>


struct device {
    int vend;
    int dev;
};
struct device supported_devices[] = {
#include "enable_drivers.h"
#include "rte_pci_dev_ids.h"
};


int main()
{
	size_t device_count = sizeof(supported_devices) / sizeof(struct device);
	for (size_t i = 0; i < device_count; ++i) {
		printf("%X:%X\n", supported_devices[i].vend,
			supported_devices[i].dev);
	}
	return 0;
}
