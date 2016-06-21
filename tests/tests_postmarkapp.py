from vendors import PostmarkApp

import unittest

class TestPostageApp(unittest.TestCase):
    def setUp(self):
        self.vendor = PostmarkApp()

    def test_ZeroEmails(self):
        self.assertEqual(self.vendor.getPrice(0), 0)

    def test_10Emails(self):
        self.assertEqual(self.vendor.getPrice(10), .01)


    def test_500k_pm(self):
        self.assertEqual(self.vendor.getPrice(500000), 500)

    def test_1000k_pm(self):
        self.assertEqual(self.vendor.getPrice(1000000), 750)

    def test_2000k_pm(self):
        self.assertEqual(self.vendor.getPrice(2000000), 1000)

    def test_5000k_pm(self):
        self.assertEqual(self.vendor.getPrice(5000000), 1250)
