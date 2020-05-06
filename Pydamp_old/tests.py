#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:24:32 2020

@author: vinny
"""

import initial #initial questions for user
import BOM


from unittest.mock import patch
from unittest import TestCase
import unittest
import datetime




class trim_question_1(TestCase):

    @patch('builtins.input', side_effect = ['yes'])
    def test_answer_yes(self, mock_input):
        self.assertEqual(initial.trim_question_1(), 'yes')
        
    @patch('builtins.input', side_effect = ['no'])
    def test_answer_no(self, mock_input):
        self.assertEqual(initial.trim_question_1(), 'no')
        
    @patch('builtins.input', side_effect = ['maybe','maybe','maybe'])
    def test_answer_wrong(self, mock):
        self.assertEqual(initial.trim_question_1(), 'failed')
        
    @patch('builtins.input', side_effect = ['maybe','maybe','yes'])
    def test_answer_partial_fail(self, mock):
        self.assertEqual(initial.trim_question_1(), 'yes')        
        
        


class initial_questions(TestCase):

    @patch('builtins.input', side_effect = ['vinny','yes','bryony'])
    def test_answer_valid_inputs_osu_student(self, mock_input):
        self.assertEqual(initial.initial_questions().__dict__, {'name': 'vinny', 'advisor': 'bryony', 'insitution': 'OSU', 'date': datetime.datetime.now().strftime('%x')})
        
    @patch('builtins.input', side_effect = ['vinny','no','dummy_corp'])
    def test_answer_valid_inputs_non_student(self, mock_input):
        self.assertEqual(initial.initial_questions().__dict__, {'name': 'vinny', 'advisor': 'n/a', 'insitution': 'dummy_corp', 'date': datetime.datetime.now().strftime('%x')})
        
    @patch('builtins.input', side_effect = ['vinny','maybe','maybe','maybe' ])
    def test_answer_trimQ1_fail(self, mock_input):
        self.assertEqual(initial.initial_questions(), 'failed')
            
#    @patch('builtins.input', side_effect = ['vinny','maybe','maybe','yes','bryony'])
#    def test_answer_trimQ1_semi_fail(self, mock_input):
#        self.assertEqual(initial.initial_questions().__dict__, {'name': 'vinny', 'advisor': 'bryony', 'insitution': 'OSU', 'date': datetime.datetime.now().strftime('%x')})
        
    @patch('builtins.input', side_effect = ['','yes','bryony','','' ])
    def test_answer_name_fail(self, mock_input):
        self.assertEqual(initial.initial_questions(), 'failed')
        
    @patch('builtins.input', side_effect = ['vin','yes','bryony','','ny' ])
    def test_answer_name_semi_fail(self, mock_input):
        self.assertEqual(initial.initial_questions().__dict__, {'name': 'vinny', 'advisor': 'bryony', 'insitution': 'OSU', 'date': datetime.datetime.now().strftime('%x')})   
        
    @patch('builtins.input', side_effect = ['vinny','no','','','' ])
    def test_answer_insitution_fail(self, mock_input):
        self.assertEqual(initial.initial_questions(), 'failed')
        
    @patch('builtins.input', side_effect = ['vinny','no','','','dummy_corp' ])
    def test_answer_insitution_semi_fail(self, mock_input):
        self.assertEqual(initial.initial_questions().__dict__, {'name': 'vinny', 'advisor': 'n/a', 'insitution': 'dummy_corp', 'date': datetime.datetime.now().strftime('%x')})
        
    @patch('builtins.input', side_effect = ['vinny','yes','','','' ])
    def test_answer_advisor_fail(self, mock_input):
        self.assertEqual(initial.initial_questions(), 'failed')
        
    @patch('builtins.input', side_effect = ['vinny','yes','','','bryony' ])
    def test_answer_advisor_semi_fail(self, mock_input):
        self.assertEqual(initial.initial_questions().__dict__, {'name': 'vinny', 'advisor': 'bryony', 'insitution': 'OSU', 'date': datetime.datetime.now().strftime('%x')})
    
    
    
class initial_questions_2(TestCase):
# I am not sure why I need this, if I include this test with the previous class it will fail. 
# The test doesn't fail. there is something being saved thats tripping up trimq1 tests.  
        
    @patch('builtins.input', side_effect = ['vinny','maybe','maybe','yes','bryony'])
    def test_answer_trimQ1_semi_fail(self, mock_input):
        self.assertEqual(initial.initial_questions().__dict__, {'name': 'vinny', 'advisor': 'bryony', 'insitution': 'OSU', 'date': datetime.datetime.now().strftime('%x')})
    
        
class system_questions(TestCase):

    @patch('builtins.input', side_effect = ['cellphone','a mobile devices used for wireless communications','29'])
    def test_answer_valid_inputs(self, mock_input):
        self.assertEqual(initial.system_questions(),('cellphone','a mobile devices used for wireless communications',29))
        
    @patch('builtins.input', side_effect = ['cellphone','a mobile devices used for wireless communications','foo','-1','42','29'])
    def test_answer_semi_fail_inputs(self, mock_input):
        self.assertEqual(initial.system_questions(),('cellphone','a mobile devices used for wireless communications',29))
        
    @patch('builtins.input', side_effect = ['cellphone','a mobile devices used for wireless communications','-1','40','50','66'])
    def test_answer_fail_inputs(self, mock_input):
        self.assertEqual(initial.system_questions(),'fail')
        
class artifact(TestCase):

    @patch('builtins.input', side_effect = ['case','provides protection from exterior elements','50','15','yes'])
    def test_answer_valid_inputs(self, mock_input):
        self.assertEqual(BOM.artifact(),(['case','provides protection from exterior elements',50,15],True))
        
    @patch('builtins.input', side_effect = ['case','provides protection from exterior elements','-1','50','100','15','no'])
    def test_answer_semi_fail_inputs(self, mock_input):
        self.assertEqual(BOM.artifact(),(['case','provides protection from exterior elements',50,15],False))
        
        
class child_data(TestCase):

    @patch('builtins.input', side_effect = ['1'])
    def test_answer_valid_inputs(self, mock_input):
        self.assertEqual(BOM.child_data(['hi','world','foo'] ),(1))
        
    @patch('builtins.input', side_effect = ['','a','4','2'])
    def test_answer_semi_fail_inputs(self, mock_input):
        self.assertEqual(BOM.child_data(['hi','world','foo'] ),(2))
        
    
class BOM_tes(TestCase):

    @patch('builtins.input', side_effect = ['case','provides protection from exterior elements','50','15','no','0'])
    def test_answer_valid_inputs(self, mock_input):
        self.assertEqual(BOM.BOM([['System_Name']]),([['System_Name'],['case','provides protection from exterior elements',50,15,0]]))
        
    @patch('builtins.input', side_effect = ['case','provides protection from exterior elements','50','15','yes','0',
                                            'screen','provides visual','50','15','no','1'])
    def test_answer_more_BOM_inputs(self, mock_input):
        self.assertEqual(BOM.BOM([['System_Name']]),([['System_Name'],
                         ['case','provides protection from exterior elements',50,15,0],
                         ['screen','provides visual',50,15,1]]))
        
        
    
if __name__ == '__main__':
    unittest.main()


    




