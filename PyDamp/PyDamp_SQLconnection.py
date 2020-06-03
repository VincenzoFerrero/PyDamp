#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 15:49:57 2020

@author: vinny
"""

import psycopg2
import datetime


def PSQL_connect(user,password,host,port,database):

    try:
        connection = psycopg2.connect(user = user,
                                      password = password,
                                      host = host,
                                      port = port,
                                      database = database)
    
        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        #print ( connection.get_dsn_parameters(),"\n")
    
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        session = cursor.fetchone()
        #print("You are connected to - ", session,"\n")
        
        
        
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    
    return connection
    


def Contributing_institution(product_dict,SQL_connection):
    
    if product_dict['OSU_Student'] == True:
        contributing_ins = 4
        return contributing_ins
        
    else:

        cursor = SQL_connection.cursor()
        cursor.execute("select * from institution_type")
        institution_table = cursor.fetchall()
        
        for i in range(len(institution_table)):
            if product_dict['Employer'] == institution_table[i][1]:
                new_institution_index = institution_table[i][0]
                return new_institution_index
            

    # Creates index for new insitution that is +1 the latest insitution in the repo #
    new_institution_index = max([ins_index[0] for ins_index in institution_table]) + 1 
                
                
    postgres_insert_query = """ INSERT INTO institution_type (ID, INSTITUTION_TYPE) VALUES (%s,%s)"""
    record_to_insert = (new_institution_index, product_dict['Employer'])
                
    cursor.execute(postgres_insert_query, record_to_insert)
#    SQL_connection.commit()
                
    return new_institution_index




        
def User_SQL_injection(product_dict,SQL_connection):
    
    
    
    ## calling cursor and pulling entire systems table from the repo
    cursor = SQL_connection.cursor()
    cursor.execute("select * from creator_info_type")
    user_table = cursor.fetchall()
    
    
    
    
    
    # Creates index for new user that is +1 the latest user entry #
    new_user_index = max([user_index[0] for user_index in user_table]) + 1 
    
    
    product_dict['User_Name'] = product_dict['User_Name'].split()
    
    
    for i in range(len(user_table)):
        
        if product_dict['User_Name'][0] == user_table[i][1]:
            try:
                if product_dict['User_Name'][1] == user_table[i][2]:
                    print('User Data found')
                    return user_table[i]
            except:
                print('User Data found')
                return user_table[i]
            
                        
    if len(product_dict['User_Name']) == 1:
    
        new_user_data = (new_user_index,
                               product_dict['User_Name'][0],
                               '',
                               product_dict['Email'],
                               product_dict['Employer']
                               )
    else:
        new_user_data = (new_user_index,
                               product_dict['User_Name'][0],
                               product_dict['User_Name'][1],
                               product_dict['Email'],
                               product_dict['Employer']
                               )
            
    
    
    postgres_insert_query = """ INSERT INTO creator_info_type (ID,FIRST_NAME,LAST_NAME,EMAIL,AFFILIATION) VALUES (%s,%s,%s,%s,%s)"""
    
    
    record_to_insert = new_user_data
                
    cursor.execute(postgres_insert_query, record_to_insert)    
    #SQL_connection.commit()
    
    cursor.close()


    return new_user_data        
        


def System_SQL_injection(product_dict,SQL_connection):
    
    
    
    ## calling cursor and pulling entire systems table from the repo
    cursor = SQL_connection.cursor()
    cursor.execute("select * from system")
    system_table = cursor.fetchall()
    
    contributing_institution = Contributing_institution(product_dict,SQL_connection)
    
    # Creates index for new product that is +1 the latest system entry #
    new_system_index = max([sys_index[0] for sys_index in system_table]) + 1 
    
    new_system_data = (new_system_index,
                       product_dict['System_Name'],
                       product_dict['System_Type'],
                       product_dict['System_Description'],
                       contributing_institution,
                       False, # This will be changed to true upon admin review"
                       3 # Source_repo. This is 'other' future functionality may allow for new source_repos
                       )
    
    
    postgres_insert_query = """ INSERT INTO system (ID,NAME,SYSTEM_TYPE,DESCRIPTION,CONTRIBUTING_INSTITUTION,VERIFIED,"Source Repository") VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    
    
    record_to_insert = new_system_data
                
    cursor.execute(postgres_insert_query, record_to_insert)    
    #SQL_connection.commit()
    
    cursor.close()


    return new_system_data





## System and User Injection needs to be ran first to generate the system index and User index.
def BOM_SQL_injection(product_dict,SQL_connection,system_index,user_index):
    
    
    
    ## calling cursor and pulling entire artifact table from the repo
    cursor = SQL_connection.cursor()
    cursor.execute("select * from artifact")
    system_table = cursor.fetchall()
    
    
    # Creates index for new components that is +1 the latest artifact entry #
    new_artifact_index = max([sys_index[0] for sys_index in system_table]) + 1
    
    
    ## System as an artifact input 
    
    new_BOM_data = []
    
    new_artifact_data = (new_artifact_index,
                         product_dict['System_Name'],
                         None,
                         179,
                         None,
                         True,
                         product_dict['System_Description'],
                         1,
                         system_index,
                         '',
                         '',
                         None,
                         datetime.datetime.now().strftime('%x'),
                         None,
                         user_index,
                         ''
                         )
    new_BOM_data.append(new_artifact_data)
    
    postgres_insert_query = """ INSERT INTO artifact 
                                (ID,NAME,CHILD_OF_ARTIFACT,BASIS_NAME,SERIAL_ID_NUMBER,ASSEMBLY,DESCRIPTION,QUANTITY,SYSTEM,MANUFACTURER,
                                TRADEMARK,ARTIFACT_RELEASE_DATE,ENTRY_DATE,MODIFICATION_DATE,CREATOR_INFO,PART_FAMILY)
                                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    
    
    record_to_insert = new_artifact_data
                
    cursor.execute(postgres_insert_query, record_to_insert)    
    
    
    
    # This loop is to preload the BOM data in to the artifact table. This done to make sure that 
    # the foreign key function in sql plays nice with the new data. 
    # In this case if a parent artifact is referenced before it is inputed into the artifact table sql will error
    # To avoid that, the BOM indices are pre populated into the repository (but not yet committed)
    for k in range(len(product_dict['BOM'])):
        
        
        preload_artifact_index = (new_artifact_index + 1 + k,
                                  '',
                                  None,
                                  None,
                                  None,
                                  False,
                                  '',
                                  1,
                                  system_index,
                                  '',
                                  '',
                                  None,
                                  datetime.datetime.now().strftime('%x'),
                                  None,
                                  user_index,
                                  ''
                                  )

        postgres_insert_query = """ INSERT INTO artifact 
                                    (ID,NAME,CHILD_OF_ARTIFACT,BASIS_NAME,SERIAL_ID_NUMBER,ASSEMBLY,DESCRIPTION,QUANTITY,SYSTEM,MANUFACTURER,
                                    TRADEMARK,ARTIFACT_RELEASE_DATE,ENTRY_DATE,MODIFICATION_DATE,CREATOR_INFO,PART_FAMILY)
                                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        
        record_to_insert = preload_artifact_index
        cursor.execute(postgres_insert_query, record_to_insert)    
    
    
    
    for i in range(len(product_dict['BOM'])):
        
    
        
        new_artifact_data = (new_artifact_index + i + 1,
                             product_dict['BOM'][i][0],
                             new_artifact_index + int(product_dict['Assembly_Data'][i][0]),
                             product_dict['BOM'][i][2],
                             None,
                             False,
                             product_dict['BOM'][i][1],
                             1,
                             system_index,
                             '',
                             '',
                             None,
                             datetime.datetime.now().strftime('%x'),
                             None,
                             user_index,
                             '',
                             new_artifact_index + i + 1)
        
        new_BOM_data.append(new_artifact_data)
        
        
        sql = """ UPDATE artifact
                SET ID = %s,
                NAME = %s,
                CHILD_OF_ARTIFACT = %s,
                BASIS_NAME = %s,
                SERIAL_ID_NUMBER = %s,
                ASSEMBLY = %s,
                DESCRIPTION = %s,
                QUANTITY = %s,
                SYSTEM = %s,
                MANUFACTURER = %s,
                TRADEMARK = %s,
                ARTIFACT_RELEASE_DATE = %s,
                ENTRY_DATE = %s,
                MODIFICATION_DATE = %s,
                CREATOR_INFO = %s,
                PART_FAMILY = %s
                WHERE ID = %s"""

        
        record_to_insert = new_artifact_data
                    
        cursor.execute(sql, record_to_insert)    
        


    cursor.close()


    return new_BOM_data



def Function_SQL_injection(product_dict,SQL_connection,BOM):
    
    
    
    ## calling cursor and pulling entire function table from the repo
    cursor = SQL_connection.cursor()
    cursor.execute("select * from function")
    function_table = cursor.fetchall()
    

    # Creates index for new product that is +1 the latest function entry #
    new_function_index = max([func_index[0] for func_index in function_table]) 
    
    function_data = []
    
    for i in range(len(product_dict['Function_Data'])):
        for k in range(len(product_dict['Function_Data'][i])):
            
            new_function_index = new_function_index + 1
            new_function_data = (new_function_index,
                                 BOM[i][0],
                                 product_dict['Function_Data'][i][k],
                                 False,
                                 )
            function_data.append(new_function_data)
    
    
            postgres_insert_query = """ INSERT INTO function (ID,DESCRIBES_ARTIFACT,SUBFUNCTION_TYPE,SUPPORTING) 
                                    VALUES (%s,%s,%s,%s)"""
    
    
            record_to_insert = new_function_data
                
            cursor.execute(postgres_insert_query, record_to_insert)
            
    
    cursor.close()


    return function_data



def Flow_SQL_injection(product_dict,SQL_connection,BOM,function_data):
    
    
    
    ## calling cursor and pulling entire flow table from the repo
    cursor = SQL_connection.cursor()
    cursor.execute("select * from flow")
    flow_table = cursor.fetchall()
    

    # Creates index for new component flow that is +1 the latest flow entry #
    new_flow_index = max([sys_index[0] for sys_index in flow_table]) 
    
    flow_data = []
    function_data_count = 0 
    
    for i in range(len(product_dict['Flow_Data'])):
        for k in range(len(product_dict['Flow_Data'][i])):
            
            Flow_of_component = product_dict['Flow_Data'][i][k]
            
            try:
                multi_flow = len(Flow_of_component[0])
                
                for j in range(len(Flow_of_component)):
                    
                    new_flow_index = new_flow_index + 1 
                    
                    multi_flow = Flow_of_component[j]
                    
                    if multi_flow[1] == 'external':
                        input_artifact = 796
                    elif multi_flow[1] == 'internal':
                        input_artifact = 830
                    else:
                        input_artifact = BOM[multi_flow[1]][0]
                        
                    
                    if multi_flow[2] == 'external':
                        output_artifact = 796
                    elif multi_flow[2] == 'internal':
                        output_artifact = 830
                    else:
                        output_artifact = BOM[multi_flow[2]][0]

                           
                    new_flow_data = (new_flow_index,
                                     function_data[function_data_count][0],
                                     input_artifact,
                                     multi_flow[0],
                                     multi_flow[3],
                                     output_artifact,
                                     True,
                                     )
                    
                    
                    
                    flow_data.append(new_flow_data)
                    
                    
                    postgres_insert_query = """ INSERT INTO flow (ID,DESCRIBES_FUNCTION,INPUT_ARTIFACT,INPUT_FLOW,OUTPUT_FLOW,
                                                                 OUTPUT_ARTIFACT,ACTIVE) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    
    
                    record_to_insert = new_flow_data
                
                    cursor.execute(postgres_insert_query, record_to_insert)
                function_data_count = function_data_count + 1 
            
            
            except TypeError: # this is if there is not a multi flow
                if type(Flow_of_component) == bool:
                    function_data_count = function_data_count + 1 
                    continue
                else:
                    
                    if Flow_of_component[1] == 'external':
                        input_artifact = 796
                    elif Flow_of_component[1] == 'internal':
                        input_artifact = 830
                    else:
                        input_artifact = BOM[Flow_of_component[1]][0]
                        
                    
                    if Flow_of_component[2] == 'external':
                        output_artifact = 796
                    elif Flow_of_component[2] == 'internal':
                        output_artifact = 830
                    else:
                        output_artifact = BOM[Flow_of_component[2]][0]

                    new_flow_index = new_flow_index + 1      
                    new_flow_data = (new_flow_index,
                                     function_data[function_data_count][0],
                                     input_artifact,
                                     Flow_of_component[0],
                                     Flow_of_component[3],
                                     output_artifact,
                                     True,
                                     )
                    
                    function_data_count = function_data_count + 1 
                    
                    flow_data.append(new_flow_data)
                    
                    postgres_insert_query = """ INSERT INTO flow (ID,DESCRIBES_FUNCTION,INPUT_ARTIFACT,INPUT_FLOW,OUTPUT_FLOW,
                                                                 OUTPUT_ARTIFACT,ACTIVE) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
    
    
                    record_to_insert = new_flow_data
                
                    cursor.execute(postgres_insert_query, record_to_insert)
            
    
    cursor.close()

    return flow_data

