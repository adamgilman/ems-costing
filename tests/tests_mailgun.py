from vendors import MailGun

import unittest
class TestMailGun(unittest.TestCase):
    def setUp(self):
        self.vendor = MailGun()

    def test_ZeroEmails(self):
        self.assertEqual(self.vendor.getPrice(0), 0)

    def test_Zero_62000(self):
        self.assertEqual(self.vendor.getPrice(1), 0)
        self.assertEqual(self.vendor.getPrice(10000), 0)

    def test_100k_pm(self):
        self.assertEqual(self.vendor.getPrice(100000), 45.00)

    def test_180k_pm(self):
        self.assertEqual(self.vendor.getPrice(180000), 85.00)

    def test_200k_pm(self):
        self.assertEqual(self.vendor.getPrice(200000), 95.00)

    def test_500k_pm(self):
        self.assertEqual(self.vendor.getPrice(500000), 245.00)

    def test_700k_pm(self):
        self.assertEqual(self.vendor.getPrice(700000), 316.50)

    def test_1500k_pm(self):
        self.assertEqual(self.vendor.getPrice(1500000), 596.50)

    def test_7000k_pm(self):
        self.assertEqual(self.vendor.getPrice(7000000), 1399.00)
