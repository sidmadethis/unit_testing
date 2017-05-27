import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """tests name for 'name_function.py' """


    def test_first_last_name(self):
        """do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()


# import unittest and the function
# class NamesTestCase will contain tests for get_formatted_name
# you can name NamesTestCase whatever you want, but making sense is good

# unittest.TestCase is how python knows how to run the tests you write

# any method starting with test_ will be run automatically when we run the file
# the self.assertEqual is just how it sounds, are the results equal to what i write as an arg?

# unittest.main() tells python to run the test in this file
