#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 09:49:39 2020

@author: vinny
"""

import setuptools


setuptools.setup(
    name="PyDamp", # Replace with your own username
    version="0.0.14",
    author="Vincenzo Ferrero",
    author_email="ferrerov@oregonstate.edu",
    description="Python-based data addition and managment of PSQL",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=['pytest','pyyaml','psycopg2==2.7.7'],
    url="https://github.com/VincenzoFerrero/PyDamp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    data_files=[('PyDamp', ['PyDamp_Server.yaml']),
                  ('PyDamp', ['Example_Product_input.yaml'])],
)