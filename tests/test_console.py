#!/usr/bin/python3
"""test the airbnb project"""


import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

with patch('sys.stdout', new=StringIO()) as f:
    string = HBNBCommand().onecmd("help show")


class TestClassMethods(unittest.TestCase):
    """test the Airbnb project"""

    def test_help(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        string = """Quit command to exit the program\n\n"""
        self.assertEqual(string, f.getvalue())

if __name__ == '__main__':
    unittest.main()
