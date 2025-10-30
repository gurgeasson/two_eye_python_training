import unittest
from a.main import assamble_question
from a.locations import locations_and_outcomes

class TestFunctions(unittest.TestCase):

    def test_(self):
        self.assertin(locations_and_outcomes[1][0], assamble_question(locations_and_outcomes), 'wrong')

if __name__ == '__main__':
    unittest.main()
