#!/usr/bin/env python3
"""
This is the test utility
"""
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from your_module import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    '''
    This is the class for testing Nested Map function
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        '''
        This tests method returns correct output
        '''
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        '''
        This test methods raises correct exception
        '''
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    '''
    This is class for testing get_json function
    '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''
        This tests method returns correct output
        '''
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(TestCase):
    '''
    This is the class for testing memoization
    '''

    def test_memoize(self):
        '''
        This tests the memoize function
        '''

        class TestClass:
            '''
            This is the test class
            '''

            def a_method(self):
                '''
                This method to always return 42
                '''
                return 42

            @memoize
            def a_property(self):
                '''
                This return memoized property
                '''
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
