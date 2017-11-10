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
        True: ('Yes', 'YES', 'Y', 'TRUE', 'tRUE', 'true', 'On'),
        
        False: ('No', 'nO', 'N', 'n', 'false', 'False', 'off', 'oFF'),
    }
    env_var_debug = 'DEBUG'
    
    def test_debug_setting(self):
        """Check if config accepts enviroment variable DEBUG and sets it."""
        from django_docker import settings
        for result, words in self._variants.items():
            for word in words:
                # print(word, result)
                with patch.dict('os.environ', {self.env_var_debug: word}):
                    importlib.reload(settings)
                    assert self.env_var_debug in os.environ
                    self.assertEqual(settings.DEBUG, result)
                assert self.env_var_debug not in os.environ # should be True
                
if __name__ == '__main__':
    main()

