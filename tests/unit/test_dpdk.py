from unittest.mock import patch, MagicMock

from hamcrest import assert_that, is_

from dpdktest import dpdk_supported_nics, pci_id, dpdk_supports


def describe_dpdk_supported_nics():
    @patch('netifaces.interfaces', MagicMock(return_value=['eth0', 'lo', 'wlan0']))
    @patch('dpdktest.dpdk_supports', MagicMock(side_effect=[True, False, True]))
    def it_returns_all_network_interface_cards_whose_device_id_is_in_dpdk_nics_list():
        nics = dpdk_supported_nics()

        assert_that(nics, is_(['eth0', 'wlan0']))

def describe_pci_id():
    def describe_when_pci_id_variable_exists_in_uevent_file():
        @patch('dpdktest.read_lines',
            MagicMock(return_value=['var=value', 'PCI_ID=1234:5678']))
        def it_returns_variable_value():
            assert_that(pci_id('any'), is_('1234:5678'))

def describe_dpdk_supports():
    def describe_when_uevent_file_is_not_found():
        @patch('dpdktest.pci_id', MagicMock(side_effect=FileNotFoundError))
        def it_returns_false():
            assert_that(dpdk_supports('eth0'), is_(False))
