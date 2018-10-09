#!/usr/bin/env python3
# -*-coding: utf8-*-
from survey import AnonymousSurvey

question = 'which language did you first learn to speak'
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print('enter "q" at any time to exit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

print('Thank you to everyone who participated in the survey')
my_survey.show_results()