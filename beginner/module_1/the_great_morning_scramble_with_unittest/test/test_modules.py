import unittest
from scr.modules import *
from data.locations import locations_and_outcomes

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.assemble_question_result = assemble_question(locations_and_outcomes)
        self.search_location_result = search_location(1, locations_and_outcomes)

    def test_assemble_question_returns_string(self):
        class_name = type(self.assemble_question_result)
        self.assertIsInstance(self.assemble_question_result, str, f"assemble_question function returns other than dict: {class_name}")

    def test_assemble_question_returns_contains(self):
        assemble_question_return_sample = "Where do you want to look?\n1. Check in your wellies\n2"
        self.assertIn(assemble_question_return_sample, self.assemble_question_result, "sample not found in returned string")

    def test_search_location_returns_boolean(self):
        self.assertIsInstance(self.search_location_result, bool, "search_location function returns other than bool")

    def test_search_location_returns_False(self):
        self.assertIs(self.search_location_result, False, "returned boolean is not 'False'")
    
if __name__ == '__main__':
    unittest.main()
