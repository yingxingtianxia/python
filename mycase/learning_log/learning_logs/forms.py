#!/usr/bin/env python3
#__*__coding: utf8__*__
from django import forms
from .models import *

class TopicForm(forms.ModelForm):
    class Meta():
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta():
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}