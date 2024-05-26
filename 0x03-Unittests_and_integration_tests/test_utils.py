#!/usr/bin/env python3
""" Unit test for the utils module """

from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union

import unittest


class TestAccessNestedMap(unittest.TestCase):
    """Test for access nested map method """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """ test access nest map """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)
