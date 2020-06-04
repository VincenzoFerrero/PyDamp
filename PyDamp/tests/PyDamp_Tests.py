#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:05:27 2020

@author: vinny
"""

""" 
The following script is used to test the checking module of the PyDamp suite. 

"""


import pytest

import PyDamp.PyDampCheck as PyDampCheck

import yaml


## Import contains correct answers
stream = open("Example_Product_input.yaml", 'r')
input_dict = yaml.load(stream, Loader=yaml.UnsafeLoader)


## Testing user name inputs

name_fail_1 = dict(input_dict)
name_fail_2 = dict(input_dict)
name_fail_3 = dict(input_dict)

name_fail_1['User_Name'] = 123
name_fail_2['User_Name'] = '123'
name_fail_3['User_Name'] = ''


def test_check_user_name1():
    """ Non - String Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_user_name(name_fail_1)
    assert str(err_info.value) == 'Input file requires character input'
def test_check_user_name2():
    """ Forced string input but is integer """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_user_name(name_fail_2)
    assert str(err_info.value) == 'Input file requires character input'
def test_check_user_name3():
    """ Empty Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_user_name(name_fail_3)
    assert str(err_info.value) == 'Input file requires user name'


## Testing OSU studnet input
    
OSU_fail_1 = dict(input_dict)
OSU_fail_2 = dict(input_dict)


OSU_fail_1['OSU_Student'] = 123
OSU_fail_2['OSU_Student'] = ''

def test_check_OSU_Student1():
    """ Interger Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_osu_student(OSU_fail_1)
    assert str(err_info.value) == 'Input file requires yes or no input'
    
def test_check_OSU_Student2():
    """ Non - String Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_osu_student(OSU_fail_2)
    assert str(err_info.value) == 'Input file requires yes or no input'
    
## Testing Employer inputs

employer_fail_1 = dict(input_dict)
employer_fail_2 = dict(input_dict)
employer_fail_3 = dict(input_dict)

employer_fail_1['Employer'] = 123
employer_fail_2['Employer'] = '123'
employer_fail_3['Employer'] = ''


def test_check_employer1():
    """ Non - String Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_employer(employer_fail_1)
    assert str(err_info.value) == 'Input file requires character input'
    
def test_check_employer2():
    """ Forced string input but is integer """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_employer(employer_fail_2)
    assert str(err_info.value) == 'Input file requires character input'
    
def test_check_employer3():
    """ Empty Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_employer(employer_fail_3)
    assert str(err_info.value) == 'Input file requires employer name'
    

## Testing System name inputs

system_fail_1 = dict(input_dict)
system_fail_2 = dict(input_dict)
system_fail_3 = dict(input_dict)

system_fail_1['System_Name'] = 123
system_fail_2['System_Name'] = '123'
system_fail_3['System_Name'] = ''


def test_check_system_name1():
    """ Non - String Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_system_name(system_fail_1)
    assert str(err_info.value) == 'Input file requires character input'
    
def test_check_system_name2():
    """ Forced string input but is integer """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_system_name(system_fail_2)
    assert str(err_info.value) == 'Input file requires character input'
    
def test_check_system_name3():
    """ Empty Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_system_name(system_fail_3)
    assert str(err_info.value) == 'Input file requires system name'    
    
    
    
    
 ## Testing BOM inputs

BOM_fail_1 = dict(input_dict)
BOM_fail_2 = dict(input_dict)
BOM_fail_3 = dict(input_dict)
BOM_fail_4 = dict(input_dict)
BOM_fail_5 = dict(input_dict)
BOM_fail_6 = dict(input_dict)
BOM_fail_7 = dict(input_dict)
BOM_fail_8 = dict(input_dict)
BOM_fail_9 = dict(input_dict)
BOM_fail_10 = dict(input_dict)
BOM_fail_11 = dict(input_dict)
BOM_fail_12 = dict(input_dict)
BOM_fail_13 = dict(input_dict)



BOM_fail_1['BOM'] = None
BOM_fail_2['BOM'] = ['']
BOM_fail_3['BOM'] = [['protective cover of product',50,15]]
BOM_fail_4['BOM'] = [['','protective cover of product',50,15]]
BOM_fail_5['BOM'] = [[123,'protective cover of product',50,15]]
BOM_fail_6['BOM'] = [['Housing','',50,15]]
BOM_fail_7['BOM'] = [['Housing',123,50,15]]
BOM_fail_8['BOM'] = [['Housing','protective cover of product','',15]]
BOM_fail_9['BOM'] = [['Housing','protective cover of product','string',15]]
BOM_fail_10['BOM'] = [['Housing','protective cover of product',180,15]]
BOM_fail_11['BOM'] = [['Housing','protective cover of product',50,'']]
BOM_fail_12['BOM'] = [['Housing','protective cover of product',50,'string']]
BOM_fail_13['BOM'] = [['Housing','protective cover of product',50,19]]



def test_check_BOM1():
    """ Empty Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_1)
    assert str(err_info.value) == 'Input file requires BOM input'       
    
def test_check_BOM2():
    """ Empty List Input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_2)
    assert str(err_info.value) == 'component 1 entry is improperly formated.' 


def test_check_BOM3():
    """ improper length BOM input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_3)
    assert str(err_info.value) == 'component 1 entry is improperly formated.'  
    
def test_check_BOM4():
    """ Missing Component Name """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_4)
    assert str(err_info.value) == 'component 1 needs a name.' 
    
def test_check_BOM5():
    """ Interger Component Name """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_5)
    assert str(err_info.value) == 'component 1 name requires charater input.'
    
def test_check_BOM6():
    """ Missing Component Discription """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_6)
    assert str(err_info.value) == 'component 1 needs a discription.'
    
def test_check_BOM7():
    """ Interger Component Discription """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_7)
    assert str(err_info.value) == 'component 1 description requires character input.'    
          
def test_check_BOM8():
    """ Missing component basis input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_8)
    assert str(err_info.value) == 'component 1 component basis requires component basis input' 
    
def test_check_BOM9():
    """ Component basis input not a integer """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_9)
    assert str(err_info.value) == 'component 1 component basis requires integer input'     
    
def test_check_BOM10():
    """ Component basis defined out of index bounds """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_10)
    assert str(err_info.value) == 'component 1 component basis input not within range of index'    
    
def test_check_BOM11():
    """ Missing component material input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_11)
    assert str(err_info.value) == 'component 1 material requires material input'
    
def test_check_BOM12():
    """ material input not a integer """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_12)
    assert str(err_info.value) == 'component 1 material requires integer input' 
    
def test_check_BOM13():
    """ material defined out of index bounds """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_BOM(BOM_fail_13)
    assert str(err_info.value) == 'component 1 material input not within range of index'    
    
    
    
 ## Testing assemly data inputs 

assembly_fail_1 = dict(input_dict)
assembly_fail_2 = dict(input_dict)
assembly_fail_3 = dict(input_dict)
assembly_fail_4 = dict(input_dict)

assembly_fail_1['Assembly_Data'] = None
assembly_fail_2['Assembly_Data'] = [[0,2], [1], [4], [0]]
assembly_fail_3['Assembly_Data'] = [['hello'], [1], [4], [0]]
assembly_fail_4['Assembly_Data'] = [[10], [1], [4], [0]]
    
    
def test_check_assembly_data1():
    """ Assembly empty"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_assembly_data(assembly_fail_1)
    assert str(err_info.value) == 'Input file requires Assembly data input(s)'  

       
def test_check_assembly_data2():
    """ improper assembly input """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_assembly_data(assembly_fail_2)
    assert str(err_info.value) == 'assembly data for component 1 entry is improperly formated.'
    
def test_check_assembly_data3():
    """ assembly input not a interger """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_assembly_data(assembly_fail_3)
    assert str(err_info.value) == 'assembly data for component 1 requires integer assembly data input' 
    
def test_check_assembly_data4():
    """ assembly input out of bounds """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_assembly_data(assembly_fail_4)
    assert str(err_info.value) == 'assembly data for component 1 assembly data input in not in range of the BOM inputs' 
    
    
    
    
    
 ## Testing Flow data inputs 

flow_fail_1 = dict(input_dict)
flow_fail_2 = dict(input_dict)
flow_fail_3 = dict(input_dict)    
flow_fail_4 = dict(input_dict)
flow_fail_5 = dict(input_dict)
flow_fail_6 = dict(input_dict)
flow_fail_7 = dict(input_dict)
flow_fail_8 = dict(input_dict)
flow_fail_9 = dict(input_dict)
flow_fail_10 = dict(input_dict)
flow_fail_11 = dict(input_dict)
flow_fail_12 = dict(input_dict)
flow_fail_13 = dict(input_dict)
flow_fail_14 = dict(input_dict)
flow_fail_15 = dict(input_dict)
flow_fail_16 = dict(input_dict)
flow_fail_17 = dict(input_dict)
flow_fail_18 = dict(input_dict)
flow_fail_19 = dict(input_dict)
flow_fail_20 = dict(input_dict)
flow_fail_21 = dict(input_dict)
flow_fail_22 = dict(input_dict)
flow_fail_23 = dict(input_dict)
flow_fail_24 = dict(input_dict)
flow_fail_25 = dict(input_dict)

flow_fail_1['Flow_Data'] = None
flow_fail_2['Flow_Data'] = [[False,False,False],[[34,'internal',0,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,2,'external',41]]]
flow_fail_3['Flow_Data'] = [[False,False],[[34,'internal',0,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_4['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[True],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_5['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40.1,2,'external',43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_6['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[100,2,'external',43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_7['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,'wrong','external',43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_8['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,True,'external',43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_9['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,100,'external',43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_10['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'wrong',43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_11['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,10.3,43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_12['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,100,43],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_13['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external','wrong'],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_14['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',100],[7,'external','internal',7]],[40,2,'external',41]],[False,False,False]]
flow_fail_15['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[True]],[False,False,False]]
flow_fail_16['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40.1,2,'external',41]],[False,False,False]]
flow_fail_17['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[100,2,'external',41]],[False,False,False]]
flow_fail_18['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,'wrong','external',41]],[False,False,False]]
flow_fail_19['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,True,'external',41]],[False,False,False]]
flow_fail_20['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,100,'external',41]],[False,False,False]]
flow_fail_21['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,2,'wrong',41]],[False,False,False]]
flow_fail_22['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,2,10.3,41]],[False,False,False]]
flow_fail_23['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,2,100,41]],[False,False,False]]
flow_fail_24['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,2,'external','wrong']],[False,False,False]]
flow_fail_25['Flow_Data'] = [[False,False,False],[[34,'internal',3,40]],[[[40,2,'external',43],[7,'external','internal',7]],[40,2,'external',100]],[False,False,False]]


def test_check_flow_data1():
    """ no flow data """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_1)
    assert str(err_info.value) == 'Input file requires Flow data input(s)'   

def test_check_flow_data2():
    """ missing flow data for one component """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_2)
    assert str(err_info.value) ==  'There is not alteast one flow datum for each component.'
    
def test_check_flow_data3():
    """ mising flow for one function """
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_3)
    assert str(err_info.value) == 'component 1 flow data input in not in range of the function inputs or is not formatted correctly'
    
    
    

""" The Following tests are for a component that has multiple flows"""   
def test_check_flow_data4():
    """ error in defining false or unknown flow"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_4)
    assert str(err_info.value) == 'component 3 has error in false naming if flow is unknown or must be an integer'    
  
def test_check_flow_data5():
    """ input flow type not an integer"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_5)
    assert str(err_info.value) == 'Flow data for component 3 function 1 needs to be an integer.'
    
def test_check_flow_data6():
    """ input flow out of flow index"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_6)
    assert str(err_info.value) == 'component 3 function 1 input in not in range of the flow index'

def test_check_flow_data7():
    """ input flow component is unknown but the string is wrong"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_7)
    assert str(err_info.value) ==  'component 3 function 1 input error for assigning internal or external'
    
def test_check_flow_data8():
    """ input flow component is not an interger or unknown"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_8)
    assert str(err_info.value) ==  'Flow data for component 3 function 1 needs to be an integer, internal, or external.'
        
def test_check_flow_data9():
    """ input flow component is out of bounds"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_9)
    assert str(err_info.value) ==  'component 3 function 1 input in not in range of the BOM inputs'

def test_check_flow_data10():
    """ output flow component is unknown but the string is wrong"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_10)
    assert str(err_info.value) == 'component 3 function 1 input error for assigning internal or external'
    
def test_check_flow_data11():
    """ output flow component is not an interger or unknown"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_11)
    assert str(err_info.value) ==  'Flow data for component 3 function 1 needs to be an integer, internal, or external.'
        
def test_check_flow_data12():
    """ output flow component is out of bounds"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_12)
    assert str(err_info.value) ==  'component 3 function 1 input in not in range of the BOM inputs'
       
def test_check_flow_data13():
    """ output flow type not an integer"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_13)
    assert str(err_info.value) == 'Flow data for component 3 function 1 needs to be an integer.'
    
def test_check_flow_data14():
    """ output flow out of flow index"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_14)
    assert str(err_info.value) == 'component 3 function 1 input in not in range of the flow index'

    
""" The Following tests are for a component that has a single flow"""   
def test_check_flow_data15():
    """ error in defining false or unknown flow"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_15)
    assert str(err_info.value) == 'component 3 function 2 has error in false naming if function is unknown or must be an integer'
  
def test_check_flow_data16():
    """ input flow type not an integer"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_16)
    assert str(err_info.value) == 'Flow data for component 3 function 2 needs to be an integer.'
    
def test_check_flow_data17():
    """ input flow out of flow index"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_17)
    assert str(err_info.value) == 'component 3 function 2 input in not in range of the flow index'

def test_check_flow_data18():
    """ input flow component is unknown but the string is wrong"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_18)
    assert str(err_info.value) ==  'component 3 function 2 input error for assigning internal or external'
    
def test_check_flow_data19():
    """ input flow component is not an interger or unknown"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_19)
    assert str(err_info.value) ==  'Flow data for component 3 function 2 needs to be an integer, internal, or external.'
        
def test_check_flow_data20():
    """ input flow component is out of bounds"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_20)
    assert str(err_info.value) ==  'component 3 function 2 input in not in range of the BOM inputs'

def test_check_flow_data21():
    """ output flow component is unknown but the string is wrong"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_21)
    assert str(err_info.value) == 'component 3 function 2 input error for assigning internal or external'
    
def test_check_flow_data22():
    """ output flow component is not an interger or unknown"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_22)
    assert str(err_info.value) ==  'Flow data for component 3 function 2 needs to be an integer, internal, or external.'
        
def test_check_flow_data23():
    """ output flow component is out of bounds"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_23)
    assert str(err_info.value) ==  'component 3 function 2 input in not in range of the BOM inputs'
       
def test_check_flow_data24():
    """ output flow type not an integer"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_24)
    assert str(err_info.value) == 'Flow data for component 3 function 2 needs to be an integer.'
    
def test_check_flow_data25():
    """ output flow out of flow index"""
    with pytest.raises(AssertionError) as err_info:
        PyDampCheck.check_flow_data(flow_fail_25)
    assert str(err_info.value) == 'component 3 function 2 input in not in range of the flow index'  
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
