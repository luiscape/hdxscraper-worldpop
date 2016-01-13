#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for the WorldPop class.

'''
import unittest

from collector.classes.worldpop import WorldPop

class TestWorldPopClass(unittest.TestCase):
  '''
  Tests for the WorldPop class.

  '''
  def setUp(self):
    self.keys = ['instance', 'success', 'data', 'key']
    self.wp = WorldPop()
    self.basic_info = WorldPop().info()

  def test_class_information_is_dictionary(self):
    '''
    Class method info() returns dictionary.

    '''
    result = self.basic_info
    self.assertIs(type(result), dict)

  def test_class_information_has_right_keys(self):
    '''
    Class method info() has right keys.

    '''
    result = self.basic_info
    for key in self.keys:
      self.assertIn(key, result.keys())

  def test_class_information_success_is_boolean(self):
    '''
    Class method info() returns boolean.

    '''
    result = self.basic_info
    self.assertIs(type(result['success']), bool)

  def test_class_worldpop_successfully_receives_data(self):
    '''
    WorldPop class successfully receives JSON data.

    '''
    result = self.basic_info
    print(result)
    self.assertIs(type(result['data']), dict)

  def test_dataset_method_returns_a_list(self):
    '''
    Tests that the datasets() method returns a list.

    '''
    result = self.wp.datasets()
    self.assertIs(type(result), list)

