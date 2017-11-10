"""Test Enviromental setting are handled properly."""


import os
import importlib
from unittest.mock import patch
# from django.test import TestCase
# from unittest import skip
"""
We have to use tools outside of Django, when it initializes 
it's too late to change enviroment variables
"""
from unittest import TestCase, main

class DebugSettingTest(TestCase):
    """Test if setting DEBUG is handled properly."""
    
    _variants = {
        True: ('Yes', 'YES', 'Y', 'TRUE', 'tRUE')
    }

