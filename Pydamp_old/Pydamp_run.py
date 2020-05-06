#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:46:43 2020

@author: vinny
"""

## Runfile for package

import datetime
import initial #initial questions for user
import BOM




if __name__ == '__main__':
    initial.welcome()
    
    user_information = initial.initial_questions()
    
    print('')
    print('Nice to meet you', user_information.name)
    print('It seems that you are from', user_information.insitution)
    print('Your advisor is', user_information.advisor)
    print('You accessed this package on', user_information.date)
    
    adding_products = True
    global_BOM = []
    
    while adding_products == True:
        
        system_information = initial.system_questions()
      
        print('')
        print('The product you are adding is: ',system_information[0])
    
        component_BOM = BOM.BOM([[system_information[0]]])
        
        end_prompt = []
        while end_prompt != 'yes' and end_prompt != 'no':
                
            end_prompt = input('Are you adding another Product?: ')
            
            if end_prompt == 'no':
                print('Thank you for using PyDamp')
                print('This session ended at: ',datetime.datetime.now().strftime('%c'))
                adding_products = False
                global_BOM.append(component_BOM)
            elif end_prompt == 'yes':
                adding_products == True
                global_BOM.append(component_BOM)
            
            else:
                print('Input invalid. Please enter yes or no')
                
            