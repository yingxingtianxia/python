#!/usr/bin/env python3
# -*-coding: utf8-*-
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = 'which language did you first learn to speak'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('english')

        self.assertIn('english', my_survey.responses)


unittest.main()
