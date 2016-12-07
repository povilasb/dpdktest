=====
About
=====

.. image:: https://travis-ci.org/povilasb/dpdktest.svg?branch=master
    :target: https://travis-ci.org/povilasb/dpdktest
.. image:: https://coveralls.io/repos/github/povilasb/dpdktest/badge.svg?branch=master
    :target: https://coveralls.io/github/povilasb/dpdktest?branch=master

This is a small tool that tests if you have NICs (Network Interface Cards)
that are supported by http://dpdk.org/ framework.

It works only on python 3::

    $ pip3 install dpdktest

How It Works?
=============

First of all supported devices vedor:device ID list is constructed from
`rte_pci_dev_ids.h
<https://github.com/scylladb/dpdk/blob/cc7e6ed22c0fc08e3ff37b3e68a61979d8214547/lib/librte_eal/common/include/rte_pci_dev_ids.h>`_.

Then `dpdktest` find all network interfaces in your computer, gets
vendor:device ID pairs for every interfaces and checks if ID is in
**dpdktest/supported_devices.txt**.
