from vendors import CritSend

import unittest

class TestPostageApp(unittest.TestCase):
    def setUp(self):
        self.vendor = CritSend()

    def test_ZeroEmails(self):
        self.assertEqual(self.vendor.getPrice(0), 0)

    def test_100k_pm(self):
        self.assertEqual(self.vendor.getPrice(100000), 50)

    def test_500k_pm(self):
        self.assertEqual(self.vendor.getPrice(500000), 250)

    def test_3000k_pm(self):
        self.assertEqual(self.vendor.getPrice(3000000), 990)

    def test_10000k_pm(self):
        self.assertEqual(self.vendor.getPrice(10000000), 3000)

    def test_50000k_pm(self):
        self.assertEqual(self.vendor.getPrice(50000000), 14000)
