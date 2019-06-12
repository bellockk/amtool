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
from render import render


class Test_AMT(unittest.TestCase):
    def test_render(self):
        pass


if __name__ == '__main__':
    unittest.main()
