# https://docs.python.org/2/library/unittest.html
import unittest

from tweet_text import idle_text, reply

# The basic building blocks of unit testing are test cases
# single scenarios that must be set up and checked for correctness.
# In unittest, test cases are represented by instances of unittest's TestCase class.
# To make your own test cases you must write subclasses of TestCase.

class TestTweetText(unittest.TestCase):

    def test_idle(self):
        # In order to test something, we use one of the assert*()
        # methods provided by the TestCase base class
        # https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertTrue
        self.assertTrue( isinstance(idle_text(), str) )

    def test_math1(self):
        response = reply({'text': '1+1', 'user': {'screen_name': 'TestUser'}})
        self.assertTrue("2" in response)

        response = reply({'text': '@bot 1+1', 'user': {'screen_name': 'TestUser'}})
        self.assertTrue("2" in response)

        response = reply({'text': 'Which Pokemon is #1', 'user': {'screen_name': 'TestUser'}})
        self.assertTrue("Bulbasaur" in response)

        response = reply({'text': 'Which Pokemon is #2', 'user': {'screen_name': 'TestUser'}})
        self.assertTrue("Ivysaur" in response)

        response = reply({'text': '@bot oh rly?', 'user': {'screen_name': 'TestUser'}})
        self.assertTrue("YA RLY!" in response)

        
if __name__ == '__main__':
    unittest.main(verbosity=2)
