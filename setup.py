from setuptools import setup


def requirements() -> list:
    with open('requirements/prod.txt') as f:
        return [l.strip() for l in f.readlines()]


setup(
    name='dpdktest',
    version='0.1.0',
    description='Tool to test if your NIC is supported by DPDK framework.',
    long_description=open('README.rst').read(),
    url='https://github.com/povilasb/dpdktest',
    author='Povilas Balciunas',
    author_email='balciunas90@gmail.com',
    license='MIT',
    packages=['dpdktest'],
    package_data={'dpdktest': ['supported_devices.txt']},
    entry_points={
        'console_scripts': ['dpdktest = dpdktest.__main__:main']
    },
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'Development Status :: 3 - Alpha',
    ],
    install_requires=requirements(),
)
