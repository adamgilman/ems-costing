from vendors import PostageApp

import unittest

class TestPostageApp(unittest.TestCase):
    def setUp(self):
        self.vendor = PostageApp()

    def test_ZeroEmails(self):
        self.assertEqual(self.vendor.getPrice(0), 9)

    def test_Zero_10000(self):
        self.assertEqual(self.vendor.getPrice(1), 9)
        self.assertEqual(self.vendor.getPrice(10000), 9)
        self.assertEqual(self.vendor.getPrice(11000), 10)

    def test_40k_pm(self):
        self.assertEqual(self.vendor.getPrice(40000), 29)
        self.assertEqual(self.vendor.getPrice(41000), 30)

    def test_100k_pm(self):
        self.assertEqual(self.vendor.getPrice(100000), 79)
        self.assertEqual(self.vendor.getPrice(101333), 80)

    def test_400k_pm(self):
        self.assertEqual(self.vendor.getPrice(400000), 199)
        self.assertEqual(self.vendor.getPrice(401333), 200)

    def test_500k_pm(self):
        self.assertEqual(self.vendor.getPrice(500000), 274)

    def test_700k_pm(self):
        self.assertEqual(self.vendor.getPrice(700000), 424)
