#!/usr/bin/env python
from setuptools import setup, find_packages

setup (
    name = "katdal",
    version = "trunk",
    description = "Karoo Array Telescope data access library to interact with HDF5 and MS files",
    author = "Ludwig Schwardt",
    author_email = "ludwig@ska.ac.za",
    packages = find_packages(),
    scripts = [
        "scripts/h5list.py",
        "scripts/h5toms.py",
        "scripts/fix_ant_positions.py",
    ],
    url='http://ska.ac.za/',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    platforms = [ "OS Independent" ],
    keywords="kat kat7 ska",
    zip_safe = False,
    # Bitten Test Suite
    test_suite = "katdal.test.suite",
)
