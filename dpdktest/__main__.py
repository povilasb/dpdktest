import sys

from dpdktest import dpdk_supported_nics


def main():
    nics = dpdk_supported_nics()
    if nics:
        print('NICs supported by DPDK:', nics)
    else:
        print("You don't have NICs supported by DPDK")
        sys.exit(-1)


if __name__ == '__main__':
    main()
