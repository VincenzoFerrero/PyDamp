#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 14:28:23 2020

@author: vinny
"""

from unittest.mock import patch
from unittest import TestCase
import unittest


def get_input(text):
    return input(text)


def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    if ans == 'no':
        return 'you entered no'


class Test(TestCase):

    # get_input will return 'yes' during this test
    @patch('builtins.input', return_value = 'yes')
    def test_answer_yes(self, mock_input):
        self.assertEqual(answer(), 'you entered yes')

    # get_input will return 'yes' during this test
    @patch('builtins.input', return_value = 'no')
    def test_answer_no(self, mock_input):
        self.assertEqual(answer(), 'you entered no')

        
if __name__ == '__main__':
    unittest.main()