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
import sys


try:
    import PyDamp.PyDamp_SQLconnection as osu_design_repo
    import PyDamp.PyDampCheck as Check
except:
    import PyDamp_SQLconnection as osu_design_repo
    import PyDampCheck as Check
    
    


try: 
    product_YAML = sys.argv[1]
    connection_YAML = sys.argv[2]
    
    if len(sys.argv) >= 4:
        sys.exit('Error: Too many input arguments.')
        
    else:
            
            
        """ The YAML import of product information """
         ## Add functionality to run this YAML from the command prompt ##
        stream = open(str(product_YAML), 'r')
        product_dict = yaml.load(stream, Loader=yaml.UnsafeLoader)
            
            
        """ The YAML import of server information """
            ## Add functionality to run this YAML from the command prompt ##
        stream = open(str(connection_YAML), 'r')
        server_info = yaml.load(stream, Loader=yaml.UnsafeLoader)
    
except Exception:
        
    if len(sys.argv) == 1:
        print('Test run of PyDamp_Run module')
        print('')
    

        """ The YAML import of product information """
        ## Add functionality to run this YAML from the command prompt ##
        stream = open("Example_Product_input.yaml", 'r')
        product_dict = yaml.load(stream, Loader=yaml.UnsafeLoader)
        
        
        """ The YAML import of server information """
        ## Add functionality to run this YAML from the command prompt ##
        stream = open("PyDamp_Server.yaml", 'r')
        server_info = yaml.load(stream, Loader=yaml.UnsafeLoader)


try:
    connection = osu_design_repo.PSQL_connect(server_info.get('user'),
                                              server_info.get('password'),
                                              server_info.get('host'),
                                              server_info.get('port'),
                                              server_info.get('database'))
    
except NameError:
    raise ValueError('Error in YAML input file(s). Please check the YAML file(s)')




""" Series of Checks to ensure the Product input YAML is correct (PyDampCheck.py) """


Check.check_product_YAML(product_dict)




system = osu_design_repo.System_SQL_injection(product_dict,connection)
user = osu_design_repo.User_SQL_injection(product_dict,connection)
BOM = osu_design_repo.BOM_SQL_injection(product_dict,connection,system[0],user[0])
function = osu_design_repo.Function_SQL_injection(product_dict,connection,BOM)
flow = osu_design_repo.Flow_SQL_injection(product_dict,connection,BOM,function)


connection.commit()
connection.close()
print("PostgreSQL connection is closed")
print('')
print('Product:',str(system[1]),'was successfully added to the OSU Design Repository')
            
