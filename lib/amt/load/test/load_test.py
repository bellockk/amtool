#!/usr/bin/env python
import unittest
import os
import sys

# Set Paths
TEST_PATH = os.path.dirname(os.path.realpath(__file__))
SUT_PATH = os.path.dirname(TEST_PATH)
DATA_PATH = os.path.join(TEST_PATH, 'data')

# Import SUT's
sys.path.append(SUT_PATH)
from load import load


class Test_AMT(unittest.TestCase):
    def test_load1(self):
        self.assertEqual({'test1': {'foo': 'bar'}},
                         load(os.path.join(DATA_PATH, 'test1')),
                         'File only')

    def test_load2(self):
        self.assertEqual({'say': {'test1': {'foo': 'bar'}}},
                         load(os.path.join(DATA_PATH, 'test2')),
                         'Directory with file')

    def test_load3(self):
        self.assertEqual({'you': {'say': {'test1': {'foo': 'bar'}}}},
                         load(os.path.join(DATA_PATH, 'test3')),
                         'Directory with Directory with file')


if __name__ == '__main__':
    unittest.main()
