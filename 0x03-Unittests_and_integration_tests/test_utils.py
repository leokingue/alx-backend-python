#!/usr/bin/env python3
from utils import access_nested_map
import unittest
from parameterized import parameterized
'''
0. Parameterize a unit test
Implementation the TestAccessNestedMap.test_access_nested_map
'''


class TestAccessNestedMap(unittest.TestCase):
    '''
    TestAccessNestedMap: unit test for the access_nest_map
    method
    '''
    @parameterized.expand([
        ({"a": 1], ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, excepted):
        '''
        Test Method for access_nested_map
        '''
        self.assertEqual(access_nested_map(nested_map, path), excepted)
