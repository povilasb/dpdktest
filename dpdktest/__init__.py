from typing import List
import os

from functional import seq
import netifaces


def read_lines(fname: str) -> List[str]:
    with open(fname, 'r') as f:
        return [line.strip() for line in f.readlines()]


def pci_id(nic: str) -> str:
    return seq(read_lines('/sys/class/net/{}/device/uevent'.format(nic)))\
        .map(lambda ln: ln.split('='))\
        .map(tuple)\
        .to_dict()['PCI_ID']


def package_dir() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def dpdk_devices_file() -> str:
    return os.path.join(package_dir(), 'supported_devices.txt')


def dpdk_supports(nic: str) -> bool:
    dpdk_nics = read_lines(dpdk_devices_file())
    try:
        return pci_id(nic) in dpdk_nics
    except FileNotFoundError:
        return False


def dpdk_supported_nics() -> List[str]:
    return seq(netifaces.interfaces())\
        .filter(dpdk_supports)\
        .to_list()
