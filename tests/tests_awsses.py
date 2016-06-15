from vendors import AWSSES

import unittest

class TestAWSSES(unittest.TestCase):
    def setUp(self):
        self.vendor = AWSSES()

    def test_ZeroEmails(self):
        self.assertEqual(self.vendor.getPrice(0), 0)

    def test_Zero_62000(self):
        #0-62000 are free
        self.assertEqual(self.vendor.getPrice(1), 0)
        self.assertEqual(self.vendor.getPrice(62000), 0)

    #amazon calculates costs per day instead of per month
    def test_100k_pm(self):
        self.assertEqual(self.vendor.getPrice(100000), 4)

    def test_150k_pm(self):
        self.assertEqual(self.vendor.getPrice(150000), 9)

    def test_200k_pm(self):
        self.assertEqual(self.vendor.getPrice(200000), 14)
