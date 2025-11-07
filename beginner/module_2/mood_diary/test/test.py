import unittest
import os

class TestDiaryEntryFile(unittest.TestCase):

    def setUp(self):
        self.NAME= "Nemo"
        self.MOOD = "not too bad"
        TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), "../mood_diary" , "2025-10-30.txt")
        with open(TESTDATA_FILENAME, "r", encoding="utf-8") as file:
            self.testdata = file.read()

    def tearDown(self):
        pass

    def test_output_is_string(self):
        self.assertIsInstance(self.testdata, str)

    def test_diary_entry_contains_name(self):
        self.assertIn(self.NAME, self.testdata, f"'{self.NAME}' is not in diary entry")

    def test_diary_entry_contains_mood(self):
        self.assertIn(self.MOOD, self.testdata, f"{self.MOOD}' is not in diary entry")

    def test_diary_entry_starts_with_dear_diary(self):
        KEY = "Dear diary"
        key_len = len(KEY)
        first_n_char_of_entry = self.testdata[:key_len]
        self.assertEqual(KEY, first_n_char_of_entry, f"Diary entry does not start with '{KEY}'")
        
        ''' much simpler way:
        self.assertTrue(self.testdata.startswith("Dear diary"))
        '''

if __name__ == "__main__":
    unittest.main()
