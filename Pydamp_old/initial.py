#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:32:39 2020

@author: vinny
"""

## This modules serves as the launch pad for entering data into the OSU repository##
## Here we collecting META data on the user, and aiding in providing the correct prompts
## through an intial quesiton set. 

import datetime

## Identifying the USER object, and required information ##
class user_information: 
    def __init__(self, name, advisor, insitution, date):
        self.name = name
        self.advisor = advisor
        self.insitution = insitution
        self.date = date 
        
        
        
def welcome():
    version = 'alpha v 0.0.1'
    print("Welcome to PyDamp, this package allows users to apply new data to exisiting Postgres repositories")
    print('')
    print("current version is ", version)
    print('')
    print('Currently this package only operates for adding products to the OSU Design Repository' )
    print('')
    print('PyDamp requres Python 3.6+')
        
#Fail count for number of attempts on a looping questions #
#fail_count is used as a global varible through out package
        
fail_count = 0 

def trim_question_1():
    ## This question establishs the user and subsiquent intial questions
    global fail_count
    trim_1 = input("Are you an OSU Student? (only answer yes or no): ")
    
    if trim_1 != 'yes' and trim_1 != 'no':
        while trim_1 != 'yes' and trim_1 != 'no':
             print('')
             fail_count = fail_count + 1 
             
             if fail_count >= 3:
                 print ('Three failed attemps. please rerun the package and visit the documentation.')
                 trim_1 = 'failed'
                 return trim_1
             else:  
                 print('')
                 print('Incorrect response please answer yes or no.')
                 trim_1 = input("Are you an OSU Student? (only answer yes or no): ")  
        fail_count = 0
        return trim_1 
          
    else:
        fail_count = 0
        return trim_1        


    
    
# look into pulling from excel or csv, so that editing quesitons is organic##        
def initial_questions():
    
#    global name
#    global insitution
#    global advisor
#    
    name = []
    insitution = []
    advisor = []
    
    name = input("Please enter name : ")
    
    trim_q1 = trim_question_1()
    
    if trim_q1 == 'failed':
        return trim_q1
    elif trim_q1 == 'yes':
        insitution = 'OSU'
        advisor = input('Who is your advisor? :')
    elif trim_q1 == 'no':
        insitution = input('What entity do you represent? :')
        advisor = 'n/a'

        
    while len(name) == 0 or len(insitution) == 0 or len(advisor) == 0:
        
        if len(name) == 0:
            fail_count = 0
            while len(name) == 0:
                fail_count = fail_count + 1
                if fail_count == 3:
                    name = 'failed'
                    print('')
                    print ('Three failed attemps. please rerun the package and visit the documentation.')
                    return name
                else:
                    print ('')
                    print ('Valid name not provided.')
                    print ('')
                    name = input("Please enter name : ")
                    
        elif len(insitution) == 0: 
           fail_count = 0
           while len(insitution) == 0:
               fail_count = fail_count + 1
               if fail_count == 3:
                    insitution = 'failed'
                    print('')
                    print ('Three failed attemps. please rerun the package and visit the documentation.')
                    return insitution
               else:
                    print ('')
                    print('Valid insitution not provided, please try again.') 
                    insitution = input('What entity do you represent? :')
                
        elif len(advisor) == 0: 
           fail_count = 0
           while len(advisor) == 0:
               fail_count = fail_count + 1
               if fail_count == 3:
                    advisor = 'failed'
                    print('')
                    print ('Three failed attemps. please rerun the package and visit the documentation.')
                    return advisor
               else:
                    print ('')
                    print('Advisor not provided, please try again.') 
                    advisor = input('Who is your advisor? :')
  
    return user_information(name, advisor, insitution, datetime.datetime.now().strftime('%x'))
        

# This looks at asking the user about general information of the product they wish to add    
def system_questions():     
    
    print('')
    print('In the current verison of PyDamp you can only add products to the OSU Design Repository.')
    print('')
    
#    user_prompt = input('Do you wish to add a product to the OSU Design Repository? /n')
#    
#    if user_pr
    
    system = input('What is the name of the product? ')
    print('')
    system_description = input('Concisely describe the product: ')

 
    system_type_list  = ['null','consumer','industrial','aerospace','scientific','biological','failure','home and garden','toys, kids and baby','sports and outdoors','electronics and computer',
                         'tools and automotive','health and beauty','tools and automotive','plants','animals','office','small appliances','garden','major appliances','entertainment',
                         'computer hardware','automotive','tools','powertools','hardware','hygiene','appliance','medical','cellular','miscellaneous']
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(system_type_list)))    

    success = False
    trys = 0
    while success == False:
        try:
            system_type = int(input('Using the system types above, what number most fits your product type? '))
            if system_type > 29 or system_type < 0:
                if trys >= 2:
                    print('Number of attempts reached. Please rerun the package and visit the documentation.')
                    return 'fail'
                else:
                    print('Number inputed not found on supplied list. Try again...')
                    trys = trys + 1 
            else:
                success = True
        except ValueError:
            print( 'That was not a valid number.  Try again...')
            
        
            
        
    return system,system_description,system_type
    
    

#Welcome()    
#print(initial_questions().__dict__)
#trim_question_1()
#system_questions()
    
