#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:08:29 2020

@author: vinny
"""

""" This is the PyDamp run module."""

## Are denoted as TO DO for the following versions

# Are denoted as author comments #

""" Are denoted for user information """


import yaml
import psycopg2
import PyDamp_SQLconnection as osu_design_repo




""" The YAML import of product information """
## Add functionality to run this YAML from the command prompt ##
stream = open("Example_Product_input.yaml", 'r')
product_dict = yaml.load(stream, Loader=yaml.UnsafeLoader)


""" The YAML import of product information """
## Add functionality to run this YAML from the command prompt ##
stream = open("PyDamp_Server.yaml", 'r')
server_info = yaml.load(stream, Loader=yaml.UnsafeLoader)



connection = osu_design_repo.PSQL_connect(server_info.get('user'),
                                          server_info.get('password'),
                                          server_info.get('host'),
                                          server_info.get('port'),
                                          server_info.get('database'))

cursor = connection.cursor()
cursor.execute("select * from system")
system_table = cursor.fetchall()