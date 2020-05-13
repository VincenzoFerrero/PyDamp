#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:49:57 2020

@author: vinny
"""

import psycopg2



def PSQL_connect(user,password,host,port,database):

    try:
        connection = psycopg2.connect(user = user,
                                      password = password,
                                      host = host,
                                      port = port,
                                      database = database)
    
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")
    
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        session = cursor.fetchone()
        print("You are connected to - ", session,"\n")
        
        
        
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    
    return connection
    










#finally:
#    #closing database connection.
#        if(connection):
#            cursor.close()
#            connection.close()
#            print("PostgreSQL connection is closed")
            
            
            
#            
#sys_index = [i[0] for i in system_table]
#sys_index.sort()
#
#
# connection = psycopg2.connect(user = "postgres",
#                                      password = "password",
#                                      host = "127.0.0.1",
#                                      port = "5432",
#                                      database = "osu_design_repo_local")
        
        
#                cursor.execute("select * from system")
#        system_table = cursor.fetchall()