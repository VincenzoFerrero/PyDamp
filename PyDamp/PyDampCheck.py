#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:42:09 2020

@author: vinny
"""

import yaml

stream = open("Example_Product_input.yaml", 'r')
product_dict = yaml.load(stream, Loader=yaml.UnsafeLoader)
#for key, value in product_dict.items():
#   print (key + " : " + str(value))
        
        
def check_user_name(product_dict):
    
    
    """ This function seperates the User input section of the YAML and checks for errors
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """
    
    #User name assertions
    User_Name = product_dict.get('User_Name','')
    assert User_Name, 'Input file requires user name'
    
    User_Name = product_dict.get('User_Name')
    assert type(User_Name) == str, 'Input file requires character input'
    
    try:
        int(product_dict.get('User_Name'))
        User_Name = int(product_dict.get('User_Name'))
        assert type(User_Name) == str, 'Input file requires character input'
        
    except ValueError:
            pass

   
    
def check_osu_student(product_dict):
    
    
    """ This function seperates the OSU_Student section of the YAML and checks for errors
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """
    
    #OSU student assertions
    
    OSU_Student = product_dict.get('OSU_Student')
    assert type(OSU_Student) == bool, 'Input file requires yes or no input'



def check_employer(product_dict):
    
    
    """ This function seperates the employer input section of the YAML and checks for errors
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """
    
    #Employer assertions
    Employer = product_dict.get('Employer','')
    assert Employer, 'Input file requires employer name'
    
    Employer = product_dict.get('Employer')
    assert type(Employer) == str, 'Input file requires character input'
    
    try:
        int(product_dict.get('Employer'))
        Employer = int(product_dict.get('Employer'))
        assert type(Employer) == str, 'Input file requires character input'
        
    except ValueError:
        pass

def check_system_name(product_dict):
    
    
    """ This function checks for errors in the system name input
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """
    
    #System name assertions
    System_Name = product_dict.get('System_Name','')
    assert System_Name, 'Input file requires system name'
    
    System_Name = product_dict.get('System_Name')
    assert type(System_Name) == str, 'Input file requires character input'
    
    try:
        int(product_dict.get('System_Name'))
        System_Name = int(product_dict.get('System_Name'))
        assert type(System_Name) == str, 'Input file requires character input'
        
    except ValueError:
        pass


def check_system_description(product_dict):
    
    
    """ This function checks for errors in the system decription input
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """
    
    #System decription assertions
    System_Description = product_dict.get('System_Description','')
    assert System_Description, 'Input file requires system description'
    
    System_Description = product_dict.get('System_Description')
    assert type(System_Description) == str, 'Input file requires character input'
    
    try:
        int(product_dict.get('System_Description'))
        System_Description = int(product_dict.get('System_Description'))
        assert type(System_Description) == str, 'Input file requires character input'
        
    except ValueError:
        pass


def check_system_type(product_dict):
    
    
    """ This function checks for errors in the system name input
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """
    
    #System system assertions
    System_Type = product_dict.get('System_Type','')
    assert System_Type, 'Input file requires system type'
    
    System_Type = product_dict.get('System_Type')
    assert type(System_Type) == int, 'Input file requires integer input'
    assert 1 <= System_Type <= 30, 'System type input not within range of index'
    


def check_BOM(product_dict):
    
    
    """ This function checks for errors in the BOM input
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """   
    
    #BOM assertions
    
    BOM = product_dict.get('BOM')
    assert BOM is not None, 'Input file requires BOM input'  
    
    
    BOM = product_dict.get('BOM')
    assert BOM[0] is not None, 'Input file requires BOM input'
    
    for i in range(len(BOM)):
        
        component = BOM[i]
        
        #BOM entry length assertion
        assert len(component) == 4, 'component ' + str(i+1) + ' entry is improperly formated.'
        
        
        #Component name assertions
        component_name= component[0]
        assert component_name, 'component ' + str(i+1) + ' needs a name.'
        
        assert type(component_name) == str, 'component ' + str(i+1) + ' name requires charater input.'
    
        try:
            component_name = int(component_name)
            assert type(component_name) == str, 'component ' + str(i+1) + ' name requires character input.'
            
        except ValueError:
            pass
        
        
        #Component description assertions    
        component_description = component[1]
        assert component_description, 'component ' + str(i+1) + ' needs a discription.'
        
        assert type(component_description) == str, 'component ' + str(i+1) + ' description requires character input.'
    
        try:
            component_description = int(component_description)
            assert type(component_description) == str, 'component ' + str(i+1) + ' description requires character input.'
            
        except ValueError:
            pass

        #Component basis assertions    
        component_basis = component[2]
        assert component_basis, 'component ' + str(i+1) + ' component basis requires component basis input'      
        assert type(component_basis) == int, 'component ' + str(i+1) + ' component basis requires integer input'  
        assert 1 <= component_basis <= 179, 'component ' + str(i+1) + ' component basis input not within range of index'  
        
        #Component material assertions    
        component_material = component[3]
        assert component_material, 'component ' + str(i+1) + ' material requires material input'      
        assert type(component_material) == int, 'component ' + str(i+1) + ' material requires integer input'  
        assert 1 <= component_material <= 18, 'component ' + str(i+1) + ' material input not within range of index' 
   

def check_assembly_data(product_dict):
    
    
    """ This function checks for errors in the BOM input
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """   
    
    #assembly_data assertion
    Assembly_Data = product_dict['Assembly_Data']
    assert Assembly_Data is not None, 'Input file requires Assembly data input(s)'  
    
    #assembly_data vertical dimension assertion
    BOM = product_dict.get('BOM')
    assert len(Assembly_Data) == len(BOM)
    

    # assembly_data for each component assertions
    for i in range(len(Assembly_Data)):
        
        Parent_of_component = Assembly_Data[i]
        
        #BOM entry length assertion
        assert len(Parent_of_component) == 1, 'assembly data for component ' + str(i+1) + ' entry is improperly formated.'
        assert type(Parent_of_component[0]) == int, 'assembly data for component ' + str(i+1) + ' requires integer assembly data input' 
        assert 0 <= Parent_of_component[0] <= len(BOM), 'assembly data for component ' + str(i+1) + ' assembly data input in not in range of the BOM inputs'      
 




def check_function_data(product_dict):
    
    
    """ This function checks for errors in the BOM input
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """   
    
    #function_data assertion
    Function_Data = product_dict['Function_Data']
    assert Function_Data is not None, 'Input file requires Function data input(s)'  
    
    #function_data vertical dimension assertion
    BOM = product_dict.get('BOM')
    assert len(Function_Data) == len(BOM)
    

    # assembly_data for each component assertions
    for i in range(len(Function_Data)):
        for k in range(len(Function_Data[i])):
        
            Function_of_component = Function_Data[i][k]
            
            #BOM entry length assertion
            assert type(Function_of_component) == int, 'Function data for component ' + str(i+1) + ' entry is improperly formated.'
            assert 1 <= Function_of_component <= 53, 'component ' + str(i+1) + ' assembly data input in not in range of the Function inputs' 



def check_flow_data(product_dict):
    
    
    """ This function checks for errors in the flow input
    
    Parameters - YAML for product information .dict
    ----------

    Returns - checked product_dict
    -------
    
    """   
    
    #flow_data assertion
    Flow_Data = product_dict['Flow_Data']
    assert Flow_Data is not None, 'Input file requires Flow data input(s)'  
    
    #flow_data vertical dimension assertion
    BOM = product_dict.get('BOM')
    assert len(Flow_Data) == len(BOM), 'There is not alteast one flow datum for each component.'
    

    # flow_data for each component assertions
    for i in range(len(Flow_Data)):
        
        #component flow data verticle dimentsion assertion
        Component_Function_data = product_dict.get('Function_Data')[i]
        assert len(Flow_Data[i]) == len(Component_Function_data), 'component ' + str(i+1) + ' flow data input in not in range of the function inputs or is not formatted correctly'
        
        
        for k in range(len(Flow_Data[i])):
        
            Flow_of_component = Flow_Data[i][k]
            
            try:
                multi_flow = len(Flow_of_component[0])
                
                for j in range(len(Flow_of_component)):
                    
                    multi_flow = Flow_of_component[j]
                    if type(multi_flow[0]) == bool or type(Flow_of_component[j][0]) == str:
                        assert multi_flow == False, 'component ' + str(i+1) + ' has error in false naming if flow is unknown or must be an integer'
                        
                    else:
                        assert type(multi_flow[0]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer.'
                        assert 0 <= multi_flow[0] <= 45, 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the flow index'
                        
                        if type(multi_flow[1]) == str:
                            assert multi_flow[1] == 'internal' or multi_flow[1] == 'external', 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input error for assigning internal or external'
                        else:
                            assert type(multi_flow[1]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer, internal, or external.'
                            assert 1 <= multi_flow[1] <= len(BOM), 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the BOM inputs'
                        
                        
                        if type(multi_flow[2]) == str:
                            assert multi_flow[2] == 'internal' or multi_flow[2] == 'external', 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input error for assigning internal or external'
                        else:
                            assert type(multi_flow[2]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer, internal, or external.'
                            assert 1 <= multi_flow[2] <= len(BOM), 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the BOM inputs'
        
                        assert type(multi_flow[3]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer.'
                        assert 0 <= multi_flow[3] <= 45, 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the flow index'                                    
                    
                
                
                
            except TypeError: # this is if there is not a multi flow
                if type(Flow_of_component) == bool or type(Flow_of_component) == str:
                    assert Flow_of_component == False, 'component ' + str(i+1) + ' function ' +str(k+1) + ' has error in false naming if function is unknown or must be an integer'
                    
                elif type(Flow_of_component[0]) == bool or type(Flow_of_component[0]) == str:
                    assert Flow_of_component == False, 'component ' + str(i+1) + ' function ' +str(k+1) + ' has error in false naming if function is unknown or must be an integer'
                    
                else:
                    assert type(Flow_of_component[0]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer.'
                    assert 0 <= Flow_of_component[0] <= 45, 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the flow index'
                    
                    if type(Flow_of_component[1]) == str:
                        assert Flow_of_component[1] == 'internal' or Flow_of_component[1] == 'external', 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input error for assigning internal or external'
                    else:
                        assert type(Flow_of_component[1]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer, internal, or external.'
                        assert 1 <= Flow_of_component[1] <= len(BOM), 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the BOM inputs'
                    
                    
                    if type(Flow_of_component[2]) == str:
                        assert Flow_of_component[2] == 'internal' or Flow_of_component[2] == 'external', 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input error for assigning internal or external'
                    else:
                        assert type(Flow_of_component[2]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer, internal, or external.'
                        assert 1 <= Flow_of_component[2] <= len(BOM), 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the BOM inputs'
    
                    assert type(Flow_of_component[3]) == int, 'Flow data for component '+ str(i+1) + ' function ' + str(k+1) + ' needs to be an integer.'
                    assert 0 <= Flow_of_component[3] <= 45, 'component ' + str(i+1) + ' function ' + str(k+1) +  ' input in not in range of the flow index'                
                

                    
                
def check_product_YAML(input_dict):
    
    check_user_name(product_dict)
    check_osu_student(product_dict)
    check_employer(product_dict)
    check_system_name(product_dict)
    check_system_description(product_dict)
    check_system_type(product_dict)
    check_BOM(product_dict)
    check_assembly_data(product_dict)
    check_function_data(product_dict)
    check_flow_data(product_dict)               
            

#
#check_flow_data(product_dict)





#if __name__ == '__main__':
#
#    stream = open("Example_Product_input.yaml", 'r')
#    product_dict = yaml.load(stream, Loader=yaml.UnsafeLoader)
#for key, value in product_dict.items():
#   print (key + " : " + str(value))
