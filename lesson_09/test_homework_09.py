import unittest
import sys
import pathlib
# parent.parent.parent - three levels up
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.parent))
from functions import count_word, get_word_in_text, find_substring

text_1 = """Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth.
"""

text_2 = ""

text_3 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']


class MyTestAboutText(unittest.TestCase):

    """
    Test 1. - Positive
    The text contains the required word
    """
    def test_1_check_text(self):
        print('\n ++++++ Test 1 +++++++')
        text = text_1
        word = 'Tom'
        amount = count_word(text, word)
        self.assertNotEqual(amount, 0, "The demanded word is not found in the text")

    """
    Test 2 - Word not present
    The text does not contain the required word
    """

    def test_2_check_text(self):
        print('\n ++++++ Test 2 +++++++')
        text = text_1
        word = 'Python'
        amount = count_word(text, word)
        print(amount)
        self.assertEqual(amount, 0, "Test failed, the demanded word should not be here")

    """
    Test 3 - The text is empty
    The given word cannot be found in empty text, expected fail inside of function
    """

    @unittest.expectedFailure
    def test_3_check_text(self):
        print('\n ++++++ Test 3 +++++++')
        text = text_2
        word = 'Python'
        print(text_2)
        print(word)
        amount = count_word(text, word)
        self.assertEquals(amount, 0, "Test failed, the demanded word should not be here")

    """
    Test 4 - 
    The text is not string, expect failure
    """

    @unittest.expectedFailure
    def test_4_check_text(self):
        print('\n ++++++ Test 4 +++++++')
        text = text_3
        word = 'Python'
        amount = count_word(text, word)
        self.assertEquals(amount, 0, "Test failed, the demanded word should not be here")

    """
    Test 5 - Positive
    The text contains the required substring
    """

    def test_5_check_text(self):
        print('\n ++++++ Test 5 +++++++')
        text = text_1
        substr = 'By the time'
        index = find_substring(text, substr)
        print(index)
        self.assertNotEqual(index, -1, "The substring is not found")

    """
    Test 6 - Negative
    The text does not contain the required substring
    """

    def test_6_check_text(self):
        print('\n ++++++ Test 6 +++++++')
        text = text_1
        substr = 'Unitest in Python'
        index = find_substring(text, substr)
        print(index)
        self.assertEqual(index, -1, "The substring is not in the text ")

    """
    Text 7 - positive
    Find the given word in the text
    """
    def test_7_check_word_in_text(self):
        print('\n ++++++ Test 7 +++++++')
        text = text_1
        word = 'Tom'
        words_place = get_word_in_text(text, word)
        print(words_place)
        self.assertNotEqual(words_place, [], "List of Index in the text is empty")

    """
    Text 8 - negative
    The given word should not be found in the text
    """

    def test_8_check_word_in_text(self):
        print('\n ++++++ Test 8 +++++++')
        text = text_1
        word = 'Python'
        words_place = get_word_in_text(text, word)
        print(words_place)
        self.assertEqual(words_place, [], "List of Index in the text is empty")


if __name__ ==('__main__'):
    unittest.main()
