import unittest
from tabnanny import verbose

from dotenv import load_dotenv

from webhook.main import main

load_dotenv(verbose=True)


class TestWebEXWebhook(unittest.TestCase):

    def test_send(self):
        result = main()
        self.assertEqual(True, result)
