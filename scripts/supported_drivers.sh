#!/bin/sh
dev_ids_header=${1-rte_pci_dev_ids.h}
cat $dev_ids_header \
	| grep -E "^#define RTE_" \
	| sed -r "s:$: {vend, dev},:"
