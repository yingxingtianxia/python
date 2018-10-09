#!/usr/bin/env python3
# -*-coding: utf8-*-
import unittest
from name_founction import get_format_name

class NameTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_format_name('jainis', 'joplin')
        self.assertEqual(formatted_name, 'Jainis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_format_name(
            'wolfgang', 'mozart', 'amadeus'
        )
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
unittest.main()