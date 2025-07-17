#!/usr/bin/env python3
"""
Test Module to Unit Test the Utils Module
"""
import unittest
from unittest.mock import patch, Mock

from parameterized import parameterized

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test Class for access nested map method """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access nested map function """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for raised exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test Class for get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock_get):
        """ Test get_json function """
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response

        result = get_json(url)

        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """ Test Class for memoize """
    def test_memoize(self):
        """ Test memoize function"""
        class TestClass:
            """ Test Class for testing the memoize decorator """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        obj = TestClass()

        with patch.object(obj, 'a_method', return_value=40) as mock:
            _ = obj.a_property
            _ = obj.a_property
            mock.assert_called_once()
