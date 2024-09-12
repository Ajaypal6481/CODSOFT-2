import unittest
from chatbot import chatbot

class TestChatbot(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(chatbot('hello'), 'Hello! How can I help you?')

    def test_timings(self):
        self.assertEqual(chatbot('what are your timings?'), 'We are open from 9AM to 5PM, Monday to Friday. We are closed on weekends and public holidays.')

    def test_fallback(self):
        self.assertEqual(chatbot('blah blah'), 'I don\'t quite understand. Could you repeat that?')

if __name__ == '__main__':
    unittest.main()
