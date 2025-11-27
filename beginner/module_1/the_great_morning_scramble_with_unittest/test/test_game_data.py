import unittest
from scr.game_data import Game_data

#test data
ts0 = {}
ts1 = {1: ["1", "1", True]}
#generate big test data
ts99 = {}
for i in range(99):
    ts99[str(i+1)] = [str(i+1), str(i+1), False]

class TestFunctions(unittest.TestCase):
    ts1 = {
    1: ["1", "1", True]
    }

    def setUp(self):
        my_game_big_data = Game_data(ts99)
        self.big_result = my_game_big_data.assemble_question(ts99)

    def test_assemble_question_returns_string(self):
        my_game_small_data = Game_data(ts1)
        self.small_result = my_game_small_data.assemble_question(ts1)
        self.assertIsInstance(self.result, str, f"assemble_question function returns other than dict: {type(self.small_result)}")

    def test_assemble_question_returns_contains(self):
        assemble_question_return_sample = "Where do you want to look?\n1. 1\n2"
        self.assertIn(assemble_question_return_sample, self.big_result, "sample not found in returned string")

    # def test_search_location_returns_boolean(self):
    #     self.assertIsInstance(self.search_location_result, bool, "search_location function returns other than bool")

    # def test_search_location_returns_False(self):
    #     self.assertIs(self.search_location_result, False, "returned boolean is not 'False'")
    
if __name__ == '__main__':
    unittest.main()
