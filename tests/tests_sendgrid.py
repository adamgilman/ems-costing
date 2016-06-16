from vendors import SendGrid

import unittest

class TestSendGrid(unittest.TestCase):
    def setUp(self):
        self.vendor = SendGrid()

    def test_ZeroEmails(self):
        self.assertEqual(self.vendor.getPrice(0), 9.95)

    def test_Zero_62000(self):
        #0-62000 are free
        self.assertEqual(self.vendor.getPrice(1), 9.95)
        self.assertEqual(self.vendor.getPrice(40000), 9.95)

    #amazon calculates costs per day instead of per month
    def test_100k_pm(self):
        self.assertEqual(self.vendor.getPrice(100000), 19.95)

    def test_180k_pm(self):
        self.assertEqual(self.vendor.getPrice(180000), 79.95)

    def test_200k_pm(self):
        self.assertEqual(self.vendor.getPrice(200000), 94.95)

    def test_500k_pm(self):
        self.assertEqual(self.vendor.getPrice(500000), 299.95)

    def test_700k_pm(self):
        self.assertEqual(self.vendor.getPrice(700000), 399.95)
