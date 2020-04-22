#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:24:32 2020

@author: vinny
"""

import initial #initial questions for user


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
        
    @patch('builtins.input', side_effect = ['','yes','bryony','','vinny' ])
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
    
        

    
if __name__ == '__main__':
    unittest.main()


    




